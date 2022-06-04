# megbord_pico
Raspberry Pi Picoで動くマクロキーパッド用の説明とコードを置いています

## 概要
本キットはRaspberry Pi Picoをマイコンとして利用したHID（Human Interface Device）です。

Raspberry Pi PicoはPCに接続すると、外部ストレージとして振舞い、こちらにプログラムを保存することで制御が行える仕組みです。

USBメモリを外部メディアとして使えるPCをご用意し、Raspberry Pi Picoのセットアップを行ってください。

## 本器の組み立て
### Raspberry Pi Picoをはんだ付けします
部品配置の関係上、高さのあるタクトスイッチよりも先にPicoをはんだ付け行った方が作業が行いやすいです

左側にUSBコネクタが出る方向でランドに合わせて配置し、マスキングテープなどで固定してください
上部左から5番目（36番ピン3V3OUT）、下部右から4から7番目（14から17番ピン　GP10から13）をはんだ付けします。もちろんすべてのランドにはんだ付けをおこなってもかまいません。

### タクトスイッチをはんだ付けします
穴の配置の通りタクトスイッチをしっかり差し込み裏面からはんだ付けをしてください

## Raspberry Pi Picoのセットアップ
CircuitPythonので動くAdafruitのHIDライブラリを利用します

1. CircuitPython環境のセットアップ
    1. CircuitPython公式サイトからRPiPico用のUF2ファイルをダウンロードします。
    https://circuitpython.org/board/raspberry_pi_pico/
    2. RPiPicoの「BOOTSEL」ボタンを押しながらUSBケーブルでPCに接続します。
    3. 「BOOTSEL」ボタンを離すと、PCがRaspberry Pi PicoをUSBマスストレージ「RPI-RP2」として認識します。
    マイコンピュータに現れた「RPI-RP2」を開き、開いたフォルダに1-1でダウンロードしたUF2ファイルを上書きます。
    するとRPiPicoが再起動して、「CIRCUITPY」というストレージがマイコンピュータに現れます。
2. Adafruit_CircuitPython_HIDライブラリのインストール
  様々なオープンソースハードウェアを展開するAdafruit社のgithubよりHIDのライブラリをいくつか入手します
  https://github.com/adafruit/Adafruit_CircuitPython_HID
  
3. 
