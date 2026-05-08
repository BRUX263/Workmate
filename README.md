# YouTube Clickbait Report CLI

CLI-приложение для формирования отчётов по CSV-файлам с метриками YouTube-видео.

Приложение читает один или несколько CSV-файлов и формирует отчёт с кликбейтными видео.
## Поддерживаемый отчёт
- `clickbait`

Видео попадает в отчёт, если:

- `ctr > 15`
- `retention_rate < 40`

Отчёт сортируется по убыванию CTR.

## Установка зависимостей

```bash
pip install -r requirements.txt
```
## Пример запуска
```bash
python -m app.main \
  --files sample_data/stats1.csv sample_data/stats2.csv \
  --report clickbait
```
## Запуск тестов

```bash
pytest
```
