import os
import subprocess
import sys
import argparse
from pathlib import Path

# 変換処理
# @params   input_path: 変換元のWebMファイルのパス
# @returns  None
def convert2mp4(input_path):
    input_path = Path(input_path)
    output_path = input_path.with_suffix('.mp4')

    # 出力ファイルが既に存在する場合は、上書きを避けるために名前を変更
    if output_path.exists():
        output_path = input_path.with_name(f"{input_path.stem}_converted.mp4")

    print(f"🎬 変換開始: {input_path.name}")

    # FFmpegコマンドの組み立て
    command = [
        'ffmpeg',
        '-i', str(input_path),           # 入力ファイル
        '-c:v', 'hevc_videotoolbox',    # AppleハードウェアHEVCエンコーダー
        '-vtag', 'hvc1',                # QuickTimeにHEVCと認識させるための必須タグ
        '-pix_fmt', 'yuv420p',          # 最も互換性の高いピクセルフォーマット
        '-c:a', 'aac',                  # 音声をAACに変換
        '-b:a', '192k',                 # 音声ビットレート
        '-y',                           # 上書き確認なし
        str(output_path)                # 出力ファイル
    ]

    try:
        # 実行
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ 変換成功: {output_path.name}")
        else:
            print(f"❌ 変換失敗: {input_path.name}")
            print(f"エラーログ: {result.stderr}")
            
    except Exception as e:
        print(f"⚠️ 予期せぬエラー: {e}")

# メイン処理
# @returns  None
def main():
    parser = argparse.ArgumentParser(description="WebMをQuickTime対応のMP4に変換します。")
    parser.add_argument("path", help="変換したいファイルまたはフォルダのパス")
    args = parser.parse_args()

    target = Path(args.path).expanduser().resolve()

    if target.is_file():
        if target.suffix.lower() == '.webm':
            convert2mp4(target)
        else:
            print("指定されたファイルはWebMではありません。")
    elif target.is_dir():
        webm_files = list(target.glob('*.webm'))
        if not webm_files:
            print("フォルダ内にWebMファイルが見つかりませんでした。")
            return
        
        print(f"📂 フォルダ内の {len(webm_files)} 個のファイルを処理します。")
        for webm in webm_files:
            convert2mp4(webm)
    else:
        print("有効なパスを指定してください。")

if __name__ == "__main__":
    main()