import csv
import datetime
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Housework

class Command(BaseCommand):
    help = "Backup Housework data"

    def handle(self, *args, **options):
        # 実行時のYYYYMMDDを取得
        date = datetime.date.today().strftime("%Y%m%d")

        # 保存フォルダの相対パス
        file_path = settings.BACKUP_PATH + 'housework_' + date + '.csv'

        # 保存ディレクトリが存在しなければ作成
        os.makedirs(settings.BACKUP_PATH, exist_ok=True)

        # バックアップファイルの作成
        with open(file_path, 'w') as file:
            writer = csv.writer(file)

            # ヘッダーの書き込み
            header = [field.name for field in Housework._meta.fields]
            writer.writerow(header)

            # Houseworkテーブルの全データを取得
            houseworks = Housework.objects.all()

            # データ部分の書き込み
            for housework in houseworks:
                writer.writerow([str(housework.user),
                                 housework.title,
                                 housework.content,
                                 str(housework.photo1),
                                 str(housework.photo2),
                                 str(housework.photo3),
                                 str(housework.created_at),
                                 str(housework.updated_at)])

            # 保存ディレクトリのファイルリストを取得
            files = os.listdir(settings.BACKUP_PATH)
            # ファイルが設定数以上あれば最も古いファイルを削除
            if len(files) >= settings.NUM_SAVED_BACKUP:
                files.sort()
                os.remove(settings.BACKUP_PATH + files[0])
