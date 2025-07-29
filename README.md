# 🎬 Tool_convert_mp4_to_gif

MP4 영상을 GIF로 쉽고 빠르게 변환하는 Python 도구입니다.
입력 폴더에 mp4 파일을 넣고, 다양한 해상도·프레임·옵션을 직접 조절하며 원하는 GIF를 만들 수 있습니다.

## 📂 폴더 구조

```
input_videos/   # 변환할 mp4 파일을 넣는 폴더
output_gifs/    # 변환된 gif가 저장되는 폴더
main.py         # 변환 실행 스크립트 (옵션 직접 수정 가능)
settings.py     # 입력/출력 폴더 경로 설정
```

## 🚀 사용법

1. `input_videos` 폴더에 mp4 파일을 복사합니다.
2. `main.py`에서 원하는 옵션(fps, scale 등)을 직접 수정합니다.
3. 아래 명령어로 변환을 실행합니다:

```bash
python main.py
```

### (선택) 용량 제한 옵션

명령행 인자로 목표 용량(MB)을 지정할 수 있습니다.

```bash
python main.py 2.5   # 2.5MB 이하로 맞추기 시도
```

## ⚙️ 주요 옵션 설명 (main.py)

- `fps`   : 초당 프레임 수 (낮출수록 용량↓, 부드러움↓)
- `scale` : 가로 해상도(px, 높이는 자동 비율)
- 기타 ffmpeg 옵션도 직접 추가 가능

## 💡 팁

- 영상이 너무 크거나 용량이 초과되면 fps/scale 값을 낮춰보세요.
- GIF는 색상수, 움직임, 길이에 따라 용량이 크게 달라집니다.
- ffmpeg가 설치되어 있어야 합니다 (PATH에 등록 필요).

## 📝 예시

1. 해상도 480, 10fps로 변환 (main.py에서 직접 수정)
2. 2MB 이하로 맞추고 싶으면:
   ```bash
   python main.py 2
   ```

## 🛠️ 의존성

- Python 3.x
- ffmpeg (https://ffmpeg.org/)

## 📑 라이선스

MIT License