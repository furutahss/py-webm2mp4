# WebmToQuickTime

WebM形式の動画ファイルを、macOS標準のQuickTime PlayerやFinal Cut Proで再生・編集可能なMP4（HEVC）形式へ変換するツールです。

## 概要

WebM形式（VP9/AV1等）の動画は、macOSの標準環境では再生できないことが多くあります。

本ツールは、Appleのハードウェアエンコーダー（VideoToolbox）を利用して、画質を維持したまま高速に互換性の高いMP4形式へ変換します。

## 主な機能

- **Apple Silicon/Intel Mac最適化**: `videotoolbox` を使用し、低負荷かつ高速なエンコードを実現。
- **QuickTime完全互換**: 動画に `hvc1` タグを付与するため、変換後即座にQuickTime Playerで再生可能。
- **バッチ処理**: ファイル単体だけでなく、フォルダを指定することで中のWebMファイルを一括変換。
- **音声変換**: 音声コーデックも互換性の高いAAC（192kbps）へ自動変換。

## 環境構築

### 必須ツールのインストール

変換エンジンの核となる `ffmpeg` をインストールしてください。

```bash
# macOSの場合
brew install ffmpeg
```

## 使い方

```bash
# ファイルを個別に変換
python main.py movie.webm

# フォルダ内のすべてのWebMを一括変換
python main.py ~/Downloads/MyVideos
```

- **出力**: 元ファイルと同じ場所に `.mp4` 拡張子で生成されます。
同名のファイルがある場合は自動的にリネームして保存されます。
