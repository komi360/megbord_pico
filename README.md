# Megbord pico
Raspberry Pi Picoで動くマクロキーパッドキットの説明とコードを置いています

![Image Main](/images/megbord_mainpic.jpg)

## 概要
本キットはRaspberry Pi Picoをマイコンとして利用したHID（Human Interface Device）です  
Raspberry Pi PicoはPCに接続すると、外部ストレージとして振舞い、こちらにプログラムを保存することで制御が行える仕組みです  
セットアップの際はUSBメモリを外部メディアとして使えるPCをご用意して行ってください  
(社用PCなど外部メディアが禁止されているPCではセットアップを行うことが出来ません)

## 本器の組み立て
### Raspberry Pi Picoのはんだ付け
部品配置の関係上、高さのあるタクトスイッチよりも先にPicoをはんだ付け行った方が作業が行いやすいです

左側にUSBコネクタが出る方向でランドに合わせて配置し、マスキングテープなどで固定してください  
36番ピン（3V3OUT）、下部14～17番ピン　（GP10～GP13）をはんだ付けします

![Image Handapin](/images/megbord_handapin.png)

もちろんすべてのランドにはんだ付けをおこなってもかまいません  
下側になる赤い基板側のランドとPicoの側面の金属端子部分にはんだをするとよいです

![Image Handapic](/images/megbord_handapic.jpg)

### タクトスイッチのはんだ付け
穴の配置の通りタクトスイッチをしっかり差し込み裏面からはんだ付けをしてください  
はんだ付け後に付属のゴム脚を適当な4隅に貼ると机が傷つかなくてよいです

![Image Back](/images/megbord_back.jpg)

## Raspberry Pi Picoのセットアップ
CircuitPythonので動くAdafruitのHIDライブラリを利用します

1. CircuitPython環境のセットアップ
    1. CircuitPython公式サイトからRPiPico用のUF2ファイルをダウンロードします  
    https://circuitpython.org/board/raspberry_pi_pico/
    2. Raspberry Pi Picoの「BOOTSEL」ボタンを押しながらUSBケーブルでPCに接続します
    3. 「BOOTSEL」ボタンを離すと、PCがRaspberry Pi PicoをUSBマスストレージ「RPI-RP2」として認識します  
    マイコンピュータに現れた「RPI-RP2」を開き、開いたフォルダに1-1でダウンロードしたUF2ファイルを上書きます  
    するとRPiPicoが再起動して、「CIRCUITPY」というストレージがマイコンピュータに現れます
2. Adafruit_CircuitPython_HIDライブラリのインストール  
    様々なオープンソースハードウェアを展開するAdafruit社のgithubよりHIDのライブラリを入手します  
    https://github.com/adafruit/Adafruit_CircuitPython_HID  
    上記リポジトリのコードを落とし、adafruit_hidフォルダをそのまま「CIRCUITPY」直下のlibフォルダの中にコピーします
3. code.pyの編集  
    本リポジトリに記載のcode.py を「CIRCUITPY」直下のcode.pyに上書きします  
    こちらのcode.pyがRaspberry Pi Pico再起動後にも自動的に実行されるようになります  
    デフォルトでボタンはそれぞれ下記がで割り振られています

    + ボタン1(左上) Ctrl + Shift + Mキー (Teamsのマイクミュート)
    + ボタン2(右上) Ctrl + Shift + Eキー (Teamsの画面共有)
    + ボタン3(左下) ボリュームダウン
    + ボタン4(右下) ボリュームアップ

## キー入力のカスタマイズ
各自の利用シーンに合わせてcode.pyを書き換えることでキー入力をカスタムすることができます  
入力可能なキーの定義はライブラリにあるkeycode.pyおよびconsumer_control_code.pyに書かれているので参考にしてください  
[/lib/adafruit_hid/keycode.py](https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py)  
[/lib/adafruit_hid/consumer_control_code.py](https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/consumer_control_code.py)


