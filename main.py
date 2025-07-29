
# 표준 라이브러리 및 설정값 임포트
import sys  # 명령행 인자 처리를 위해 사용
from pathlib import Path  # 경로 처리를 위해 사용
from settings import INPUT_DIR, OUTPUT_DIR  # 설정값 임포트
import subprocess  # ffmpeg 등 외부 명령 실행을 위해 사용

def convert_mp4_to_gif(input_path, output_path, target_size_mb=None):
    """
    MP4 영상을 GIF로 변환합니다. target_size_mb가 지정되면 용량을 맞추려 시도합니다.
    input_path: 입력 mp4 파일 경로
    output_path: 출력 gif 파일 경로
    target_size_mb: 목표 용량(MB, None이면 제한 없음)
    """
    # ffmpeg 명령어 옵션 조절: 아래 값들을 직접 수정해보세요!
    fps = 30  # 초당 프레임 수 (낮출수록 용량↓, 부드러움↓)
    scale = 1000  # 가로 해상도(px), 높이는 자동 비율
    # -vf: 비디오 필터 (프레임수, 해상도, 보간법)
    # -loop 0: 무한 반복 gif
    ffmpeg_cmd = [
        'ffmpeg',  # ffmpeg 실행
        '-y',  # 기존 파일 덮어쓰기
        '-i', str(input_path),  # 입력 파일
        '-vf', f'fps={fps},scale={scale}:-1:flags=lanczos',  # 프레임수/해상도/보간법
        '-loop', '0',  # 무한 반복
        str(output_path)  # 출력 파일
    ]
    # 아래는 용량 제한 시 비트레이트 조절(실제 GIF엔 거의 영향 없음)
    if target_size_mb:
        duration = get_video_duration(input_path)  # 영상 길이(초)
        if duration > 0:
            target_size_bytes = target_size_mb * 1024 * 1024  # 목표 바이트
            bitrate = int((target_size_bytes * 8) / duration)  # 비트레이트 계산
            ffmpeg_cmd.insert(-1, f'-b:v')  # 비디오 비트레이트 옵션 추가
            ffmpeg_cmd.insert(-1, str(bitrate))
    # ffmpeg 실행 (실제 변환)
    subprocess.run(ffmpeg_cmd, check=True)

def get_video_duration(video_path):
    try:
        # ffprobe로 영상 길이(초) 추출
        result = subprocess.run([
            'ffprobe',
            '-v', 'error',
            '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1',
            str(video_path)
        ], capture_output=True, text=True, check=True)
        return float(result.stdout.strip())
    except Exception:
        return 0  # 실패 시 0 반환

def main():
    input_dir = Path(INPUT_DIR)  # 입력 폴더 경로
    output_dir = Path(OUTPUT_DIR)  # 출력 폴더 경로
    output_dir.mkdir(exist_ok=True)  # 출력 폴더 없으면 생성
    # 명령행 인자로 용량 지정 시만 적용
    target_size_mb = None
    if len(sys.argv) > 1:
        try:
            target_size_mb = float(sys.argv[1])
        except ValueError:
            print('Invalid size argument, ignoring.')
    # 입력 폴더 내 mp4 파일 반복 처리
    for file in input_dir.iterdir():
        if file.suffix.lower() == '.mp4':  # mp4만 변환
            output_gif = output_dir / (file.stem + '.gif')  # 출력 파일명
            print(f'Converting {file} to {output_gif}...')
            try:
                convert_mp4_to_gif(file, output_gif, target_size_mb)  # 변환 실행
                print(f'Success: {output_gif}')
            except Exception as e:
                print(f'Failed to convert {file}: {e}')

# 이 파일을 직접 실행하면 main() 함수가 동작합니다.
if __name__ == '__main__':
    main()
