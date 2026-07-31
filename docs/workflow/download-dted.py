#!/usr/bin/env python3
"""
download-dted.py — TRN용 DTED 지형 데이터 다운로드 스크립트

목적: VIO의 상대위치를 글로벌 좌표로 보정하기 위한 DTED(Digital Terrain Elevation Data) 다운로드.

사용법:
  python3 download-dted.py --bbox W,S,E,N --output ./maps/

예시:
  # 한국 전역 (대한민국 남서~북동)
  python3 download-dted.py --bbox 124,33,131,39 --output ./maps/

  # 작은 영역 (테스트용)
  python3 download-dted.py --bbox 126.9,37.5,127.0,37.6 --output ./maps/test/

출처:
  - NASADEM 30m (NASA Earthdata, HDF5) — 무료, NASA 계정 필요
  - SRTM 30m (USGS, GeoTIFF) — 무료, USGS 계정 필요
  - Copernicus GLO-30 (EU-DEM, GeoTIFF) — 무료

의존성:
  pip install requests

참고:
  - DTED Level 1: ~90m 해상도
  - DTED Level 2: ~30m 해상도 (대부분의 DTED가 Level 2)
  - NASADEM: SRTM의 후속, 30m 해상도, 전 세계 커버리지

NASA Earthdata 계정 생성: https://urs.earthdata.nasa.gov/
USGS 계정 생성: https://ers.cr.usgs.gov/
"""

import argparse
import os
import sys
import math
import requests
from pathlib import Path

# USGS 3DEP S3 버킷 (무료, 직접 다운로드 가능)
# 정확한 URL 패턴: https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1/TIFF/current/{lat}/{lon}.tif
USGS_S3_BASE = "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1/TIFF/current"

# NASA Earthdata NASADEM (토큰 필요)
NASADEM_BASE = "https://n5eil02u.ecs.nsidw.intl"

# OpenTopography (무료, API 키 필요)
OPENTOPO_BASE = "https://opentopography.org"


def get_tile_name(lat, lon):
    """타일 이름 생성 (예: N37E126.hgt)"""
    lat_prefix = 'N' if lat >= 0 else 'S'
    lon_prefix = 'E' if lon >= 0 else 'W'
    lat_val = int(abs(lat))
    lon_val = int(abs(lon))
    return f"{lat_prefix}{lat_val:02d}{lon_prefix}{lon_val:03d}"


def download_usgs_tile(lat, lon, output_dir, session):
    """USGS 3DEP S3 타일 다운로드 (30m, 무료)"""
    tile_name = get_tile_name(lat, lon)
    url = f"{USGS_S3_BASE}/{lat}/{lon}.tif"
    
    output_path = os.path.join(output_dir, f"{tile_name}.tif")
    if os.path.exists(output_path):
        print(f"  ✅ {tile_name}.tif already exists, skipping")
        return output_path
    
    print(f"  📥 Downloading {tile_name}.tif from USGS 3DEP S3...")
    try:
        response = session.get(url, timeout=60, stream=True)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"  ✅ Saved {tile_name}.tif ({size_mb:.1f}MB)")
            return output_path
        else:
            print(f"  ❌ HTTP {response.status_code} for {tile_name}")
    except Exception as e:
        print(f"  ❌ Error downloading {tile_name}: {str(e)[:50]}")
    
    return None


def generate_dted_grid(bbox, output_dir):
    """
    BBOX 기반 DTED 타일 다운로드
    
    Args:
        bbox: (W, S, E, N) 좌표
        output_dir: 저장할 디렉토리
    """
    W, S, E, N = bbox
    os.makedirs(output_dir, exist_ok=True)
    
    session = requests.Session()
    
    # 타일 좌표 계산 (1도 간격)
    tiles = []
    for lat in range(int(math.floor(S)), int(math.ceil(N)) + 1):
        for lon in range(int(math.floor(W)), int(math.ceil(E)) + 1):
            tiles.append((lat, lon))
    
    print(f"📍 BBOX: W={W}, S={S}, E={E}, N={N}")
    print(f"📌 타일 수: {len(tiles)}개 (약 {len(tiles) * 20}MB)")
    print(f"📁 저장 위치: {output_dir}")
    print(f"🌐 데이터 소스: USGS 3DEP S3 (30m)")
    print()
    
    downloaded = []
    failed = []
    
    for lat, lon in tiles:
        result = download_usgs_tile(lat, lon, output_dir, session)
        
        if result:
            downloaded.append(result)
        else:
            failed.append((lat, lon))
    
    print(f"\n📊 결과: {len(downloaded)}개 성공, {len(failed)}개 실패")
    return downloaded, failed


def create_dted_metadata(output_dir, bbox, downloaded_files):
    """DTED 메타데이터 파일 생성"""
    meta_path = os.path.join(output_dir, "dted_metadata.txt")
    W, S, E, N = bbox
    
    with open(meta_path, 'w') as f:
        f.write(f"# DTED Metadata\n")
        f.write(f"# Generated: {__import__('datetime').datetime.now().isoformat()}\n")
        f.write(f"# Bounding Box: W={W}, S={S}, E={E}, N={N}\n")
        f.write(f"# Source: USGS 3DEP S3 (30m / 1 Arc-Second)\n")
        f.write(f"# Tile Count: {len(downloaded_files)}\n")
        f.write(f"# Resolution: 30m (1 Arc-Second)\n")
        f.write(f"# Coordinate System: WGS84 (EPSG:4326)\n")
        f.write(f"# Usage: TRN (Terrain Referenced Navigation) for VIO drift correction\n\n")
        f.write(f"# Files:\n")
        for f_path in sorted(downloaded_files):
            f.write(f"{os.path.basename(f_path)}\n")
    
    print(f"📝 메타데이터 저장: {meta_path}")


def main():
    parser = argparse.ArgumentParser(description="TRN용 DTED 지형 데이터 다운로드")
    parser.add_argument("--bbox", required=True, 
                        help="Bounding box: W,S,E,N (예: 124,33,131,39)")
    parser.add_argument("--output", default="./maps/", 
                        help="저장할 디렉토리 (기본: ./maps/)")
    
    args = parser.parse_args()
    
    # BBOX 파싱
    try:
        coords = [float(x) for x in args.bbox.split(",")]
        if len(coords) != 4:
            raise ValueError("BBOX는 W,S,E,N 4개의 좌표가 필요합니다")
        bbox = tuple(coords)
    except ValueError as e:
        print(f"❌ BBOX 파싱 오류: {e}")
        print(f"   예시: --bbox 126.9,37.5,127.0,37.6")
        sys.exit(1)
    
    # 다운로드
    downloaded, failed = generate_dted_grid(bbox, args.output)
    
    # 메타데이터 생성
    if downloaded:
        create_dted_metadata(args.output, bbox, downloaded)
    
    # 실패한 타일 보고
    if failed:
        print(f"\n⚠️ 실패한 타일: {failed}")
        print("   → USGS TNM(https://apps.nationalmap.gov/viewer/)에서 수동 다운로드")
        print("   → 또는 NASA Earthdata(https://search.earthdata.nasa.gov/)에서 NASADEM 검색")
    
    print("\n✅ DTED 다운로드 완료!")
    print(f"   저장 위치: {args.output}")
    print(f"   사용법: TRN 스크립트에서 {args.output}/dted_metadata.txt 참조")


if __name__ == "__main__":
    main()
