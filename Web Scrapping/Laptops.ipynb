# Laptops

import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = [
    'https://www.flipkart.com/lenovo-ideapad-slim-1-amd-ryzen-5-hexa-core-5500u-16-gb-512-gb-ssd-windows-11-home-15alc7-thin-light-laptop/product-reviews/itmce54714ae1cd8?pid=COMGN2YDSFGGXYG3&lid=LSTCOMGN2YDSFGGXYG3MJBCRU&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-255-g10-2024-amd-ryzen-3-quad-core-7320u-8-gb-512-gb-ssd-windows-11-home-250-thin-light-laptop/product-reviews/itmac0cd52f844ae?pid=COMH743DRRNQYDSH&lid=LSTCOMH743DRRNQYDSHWKCNLQ&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/hp-255-g10-2024-amd-ryzen-3-quad-core-7320u-8-gb-512-gb-ssd-windows-11-home-250-thin-light-laptop/product-reviews/itmac0cd52f844ae?pid=COMH743DRRNQYDSH&lid=LSTCOMH743DRRNQYDSHWKCNLQ&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-255-g10-2024-amd-ryzen-3-quad-core-7320u-8-gb-512-gb-ssd-windows-11-home-250-thin-light-laptop/product-reviews/itmac0cd52f844ae?pid=COMH743DRRNQYDSH&lid=LSTCOMH743DRRNQYDSHWKCNLQ&marketplace=FLIPKART&page=10', 
    'https://www.flipkart.com/samsung-galaxy-book4-intel-core-i5-13th-gen-1335u-16-gb-512-gb-ssd-windows-11-home-np750xgj-kg2in-np750xgj-lg2in-thin-light-laptop/product-reviews/itm820dc496ef160?pid=COMGZUYDGFJGHZR4&lid=LSTCOMGZUYDGFJGHZR4MBHZ27&marketplace=FLIPKART',
    'https://www.flipkart.com/samsung-galaxy-book4-intel-core-i5-13th-gen-1335u-16-gb-512-gb-ssd-windows-11-home-np750xgj-kg2in-np750xgj-lg2in-thin-light-laptop/product-reviews/itm820dc496ef160?pid=COMGZUYDGFJGHZR4&lid=LSTCOMGZUYDGFJGHZR4MBHZ27&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/asus-tuf-gaming-a15-amd-ryzen-7-octa-core-7435hs-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-2050-fa566nfr-hn260w-laptop/product-reviews/itm10514ecd2a794?pid=COMHFT2NBDET7GJX&lid=LSTCOMHFT2NBDET7GJXKL60AC&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-tuf-gaming-a15-amd-ryzen-7-octa-core-7435hs-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-2050-fa566nfr-hn260w-laptop/product-reviews/itm10514ecd2a794?pid=COMHFT2NBDET7GJX&lid=LSTCOMHFT2NBDET7GJXKL60AC&marketplace=FLIPKART&page=5',
    'https://www.flipkart.com/acer-aspire-3-intel-celeron-dual-core-8-gb-512-gb-ssd-windows-11-home-a311-45-thin-light-laptop/product-reviews/itmad38595c5a902?pid=COMH7NCZY2QDJ5Z4&lid=LSTCOMH7NCZY2QDJ5Z4RHDRWI&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-aspire-3-intel-celeron-dual-core-8-gb-512-gb-ssd-windows-11-home-a311-45-thin-light-laptop/product-reviews/itmad38595c5a902?pid=COMH7NCZY2QDJ5Z4&lid=LSTCOMH7NCZY2QDJ5Z4RHDRWI&marketplace=FLIPKART&page=3',
    'https://www.flipkart.com/asus-vivobook-15-backlit-keyboard-intel-core-i3-12th-gen-1215u-8-gb-512-gb-ssd-windows-11-home-x1504za-nj321ws-thin-light-laptop/product-reviews/itmbe5bbf6a5168b?pid=COMGT2ZXC24MFNFA&lid=LSTCOMGT2ZXC24MFNFAH8MFND&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-vivobook-15-backlit-keyboard-intel-core-i3-12th-gen-1215u-8-gb-512-gb-ssd-windows-11-home-x1504za-nj321ws-thin-light-laptop/product-reviews/itmbe5bbf6a5168b?pid=COMGT2ZXC24MFNFA&lid=LSTCOMGT2ZXC24MFNFAH8MFND&marketplace=FLIPKART&page=4',
    'https://www.flipkart.com/hp-omen-amd-ryzen-7-octa-core-7840hs-16-gb-1-tb-ssd-windows-11-home-6-gb-graphics-nvidia-geforce-rtx-4050-16-xd0015ax-gaming-laptop/product-reviews/itmabad31c69922e?pid=COMH28U4QR7GUZHM&lid=LSTCOMH28U4QR7GUZHMKTPBNH&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-omen-amd-ryzen-7-octa-core-7840hs-16-gb-1-tb-ssd-windows-11-home-6-gb-graphics-nvidia-geforce-rtx-4050-16-xd0015ax-gaming-laptop/product-reviews/itmabad31c69922e?pid=COMH28U4QR7GUZHM&lid=LSTCOMH28U4QR7GUZHMKTPBNH&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/hp-victus-15-intel-core-i5-13th-gen-13420h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-15-fa1327tx-gaming-laptop/product-reviews/itmb08f154f265d7?pid=COMHY8KVZ73Y9PPY&lid=LSTCOMHY8KVZ73Y9PPYGBSHGI&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-victus-15-intel-core-i5-13th-gen-13420h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-15-fa1327tx-gaming-laptop/product-reviews/itmb08f154f265d7?pid=COMHY8KVZ73Y9PPY&lid=LSTCOMHY8KVZ73Y9PPYGBSHGI&marketplace=FLIPKART&page=7',
    'https://www.flipkart.com/chuwi-intel-celeron-quad-core-12th-gen-n100-8-gb-256-gb-ssd-windows-11-home-gemibook-plus-laptop/product-reviews/itm1a0b8c551a8e1?pid=COMGVGD39MWGVFXH&lid=LSTCOMGVGD39MWGVFXH7GJDZ8&marketplace=FLIPKART',
    'https://www.flipkart.com/chuwi-intel-celeron-quad-core-12th-gen-n100-8-gb-256-gb-ssd-windows-11-home-gemibook-plus-laptop/product-reviews/itm1a0b8c551a8e1?pid=COMGVGD39MWGVFXH&lid=LSTCOMGVGD39MWGVFXH7GJDZ8&marketplace=FLIPKART&page=5',
    'https://www.flipkart.com/colorful-p15-intel-core-i5-12th-gen-12450h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-4050-23-he55d16512a-w-ind-gaming-laptop/product-reviews/itmc8b8c723f21e7?pid=COMGZKFB9RUX32NA&lid=LSTCOMGZKFB9RUX32NAXFBCNN&marketplace=FLIPKART',
    'https://www.flipkart.com/colorful-p15-intel-core-i5-12th-gen-12450h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-4050-23-he55d16512a-w-ind-gaming-laptop/product-reviews/itmc8b8c723f21e7?pid=COMGZKFB9RUX32NA&lid=LSTCOMGZKFB9RUX32NAXFBCNN&marketplace=FLIPKART&page=3',
    'https://www.flipkart.com/msi-katana-a15-ai-amd-ryzen-7-octa-core-8845hs-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-4050-144-hz-b8ve-418in-gaming-laptop/product-reviews/itmbeb700320ffee?pid=COMGXMSXXJHW9RFJ&lid=LSTCOMGXMSXXJHW9RFJZMD4HY&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-aspire-3-intel-celeron-dual-core-n4500-8-gb-512-gb-ssd-windows-11-home-a324-45-thin-light-laptop/product-reviews/itmbbfe217e40d59?pid=COMHFZYZFVD2MCAB&lid=LSTCOMHFZYZFVD2MCABTLQNKG&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-aspire-3-intel-celeron-dual-core-n4500-8-gb-512-gb-ssd-windows-11-home-a324-45-thin-light-laptop/product-reviews/itmbbfe217e40d59?pid=COMHFZYZFVD2MCAB&lid=LSTCOMHFZYZFVD2MCABTLQNKG&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/thomson-intel-celeron-dual-core-n4020-4-gb-128-gb-ssd-windows-11-home-in-n15v2c-thin-light-laptop/product-reviews/itm877c9982f92bc?pid=COMHY9GHJSBGUGNW&lid=LSTCOMHY9GHJSBGUGNWAANV1K&marketplace=FLIPKART',
    'https://www.flipkart.com/infinix-x3-slim-intel-core-i7-12th-gen-1255u-16-gb-512-gb-ssd-windows-11-home-xl422-thin-light-laptop/product-reviews/itm1828edaca2b67?pid=COMGRSWXNS9BKMHH&lid=LSTCOMGRSWXNS9BKMHH9SNAHF&marketplace=FLIPKART',
    'https://www.flipkart.com/infinix-x3-slim-intel-core-i7-12th-gen-1255u-16-gb-512-gb-ssd-windows-11-home-xl422-thin-light-laptop/product-reviews/itm1828edaca2b67?pid=COMGRSWXNS9BKMHH&lid=LSTCOMGRSWXNS9BKMHH9SNAHF&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/infinix-gt-book-intel-core-i5-12th-gen-12450h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-80-w-gl613-gaming-laptop/product-reviews/itmc9e44d5a9f6c4?pid=COMHYS44DKVFUFVS&lid=LSTCOMHYS44DKVFUFVS2KZG86&marketplace=FLIPKART',
    'https://www.flipkart.com/infinix-gt-book-intel-core-i5-12th-gen-12450h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-80-w-gl613-gaming-laptop/product-reviews/itmc9e44d5a9f6c4?pid=COMHYS44DKVFUFVS&lid=LSTCOMHYS44DKVFUFVS2KZG86&marketplace=FLIPKART&page=7',
    'https://www.flipkart.com/asus-vivobook-s-15-oled-intel-evo-h-series-core-i5-13th-gen-13500h-16-gb-512-gb-ssd-windows-11-home-s5504va-ma541ws-thin-light-laptop/product-reviews/itm8486d594ff56b?pid=COMHYWSWHTGX8BWG&lid=LSTCOMHYWSWHTGX8BWGUIGHE6&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-vivobook-s-15-oled-intel-evo-h-series-core-i5-13th-gen-13500h-16-gb-512-gb-ssd-windows-11-home-s5504va-ma541ws-thin-light-laptop/product-reviews/itm8486d594ff56b?pid=COMHYWSWHTGX8BWG&lid=LSTCOMHYWSWHTGX8BWGUIGHE6&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/hp-255-g9-amd-ryzen-3-dual-core-3250-8-gb-512-gb-ssd-windows-11-home-g8-thin-light-laptop/product-reviews/itm087b6d1981ee8?pid=COMGFBK9A3Z2QD9H&lid=LSTCOMGFBK9A3Z2QD9HIAVQFL&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-255-g9-amd-ryzen-3-dual-core-3250-8-gb-512-gb-ssd-windows-11-home-g8-thin-light-laptop/product-reviews/itm087b6d1981ee8?pid=COMGFBK9A3Z2QD9H&lid=LSTCOMGFBK9A3Z2QD9HIAVQFL&marketplace=FLIPKART&page=9',
    'https://www.flipkart.com/lenovo-loq-amd-ryzen-5-quad-core-7235hs-24-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-15arp9-gaming-laptop/product-reviews/itmd3fbbdced2d6b?pid=COMHFYZ3FDVNVJU7&lid=LSTCOMHFYZ3FDVNVJU7JU0TVS&marketplace=FLIPKART',
    'https://www.flipkart.com/lenovo-loq-amd-ryzen-5-quad-core-7235hs-24-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-15arp9-gaming-laptop/product-reviews/itmd3fbbdced2d6b?pid=COMHFYZ3FDVNVJU7&lid=LSTCOMHFYZ3FDVNVJU7JU0TVS&marketplace=FLIPKART&page=6',
    'https://www.flipkart.com/apple-macbook-air-m2-8-gb-512-gb-ssd-mac-os-monterey-mly03hn-a/product-reviews/itm6533ea968a81e?pid=COMGFB2GTM7MMJYN&lid=LSTCOMGFB2GTM7MMJYNIHQHMG&marketplace=FLIPKART',
    'https://www.flipkart.com/apple-macbook-air-m2-8-gb-512-gb-ssd-mac-os-monterey-mly03hn-a/product-reviews/itm6533ea968a81e?pid=COMGFB2GTM7MMJYN&lid=LSTCOMGFB2GTM7MMJYNIHQHMG&marketplace=FLIPKART&page=6',
    'https://www.flipkart.com/infinix-x-air-pro-intel-core-i5-13th-gen-1334u-16-gb-512-gb-ssd-windows-11-home-xl434-thin-light-laptop/product-reviews/itmffc6afe9cedcc?pid=COMH5MKHPPTGZQZW&lid=LSTCOMH5MKHPPTGZQZWBCKVCR&marketplace=FLIPKART',
    'https://www.flipkart.com/chuwi-intel-celeron-quad-core-12th-gen-n100-8-gb-256-gb-ssd-windows-11-home-gemibook-x-pro-laptop/product-reviews/itm95998eabab6f9?pid=COMGVBZBDZJXUZFC&lid=LSTCOMGVBZBDZJXUZFCFYZTJO&marketplace=FLIPKART',
    'https://www.flipkart.com/chuwi-intel-celeron-quad-core-12th-gen-n100-8-gb-256-gb-ssd-windows-11-home-gemibook-x-pro-laptop/product-reviews/itm95998eabab6f9?pid=COMGVBZBDZJXUZFC&lid=LSTCOMGVBZBDZJXUZFCFYZTJO&marketplace=FLIPKART&page=5',
    'https://www.flipkart.com/acer-aspire-7-intel-core-i5-13th-gen-13420h-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-2050-a715-79g-gaming-laptop/product-reviews/itm8208102c97f99?pid=COMH3G96J7CE6ZPH&lid=LSTCOMH3G96J7CE6ZPHSFRCM4&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-aspire-7-intel-core-i5-13th-gen-13420h-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-2050-a715-79g-gaming-laptop/product-reviews/itm8208102c97f99?pid=COMH3G96J7CE6ZPH&lid=LSTCOMH3G96J7CE6ZPHSFRCM4&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7v4hn-a/product-reviews/itm6533ea968a81e?pid=COMH64PYUPETD5WB&lid=LSTCOMH64PYUPETD5WB801R5F&marketplace=FLIPKART',
    'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7v4hn-a/product-reviews/itm6533ea968a81e?pid=COMH64PYUPETD5WB&lid=LSTCOMH64PYUPETD5WB801R5F&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/samsung-galaxy-book4-pro-evo-ai-pc-intel-core-ultra-7-155h-16-gb-512-gb-ssd-windows-11-home-np940xgk-kg2in-np940xgk-lg2in-thin-light-laptop/product-reviews/itmbfccc677e9120?pid=COMGY2H4FQTJPRWB&lid=LSTCOMGY2H4FQTJPRWBWA2YZV&marketplace=FLIPKART',
    'https://www.flipkart.com/samsung-galaxy-book4-pro-evo-ai-pc-intel-core-ultra-5-125h-16-gb-512-gb-ssd-windows-11-home-np940xgk-ks1in-np940xgk-ls1in-thin-light-laptop/product-reviews/itmf5fa25819ad9f?pid=COMGY2H4TUHT2Z5Q&lid=LSTCOMGY2H4TUHT2Z5QKOA5PP&marketplace=FLIPKART',
    'https://www.flipkart.com/apple-macbook-air-m3-8-gb-256-gb-ssd-macos-sonoma-mryu3hn-a/product-reviews/itmb1aa0cc739560?pid=COMGYP5GMQPRAEWA&lid=LSTCOMGYP5GMQPRAEWAAADIG6&marketplace=FLIPKART',
    'https://www.flipkart.com/apple-macbook-air-m3-8-gb-256-gb-ssd-macos-sonoma-mryu3hn-a/product-reviews/itmb1aa0cc739560?pid=COMGYP5GMQPRAEWA&lid=LSTCOMGYP5GMQPRAEWAAADIG6&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/lenovo-loq-intel-core-i7-13th-gen-13650hx-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-15irx9-gaming-laptop/product-reviews/itme3e94a3f73f71?pid=COMGYSFG7JNFXNM9&lid=LSTCOMGYSFG7JNFXNM9NT4T6Z&marketplace=FLIPKART',
    'https://www.flipkart.com/lenovo-loq-intel-core-i7-13th-gen-13650hx-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-15irx9-gaming-laptop/product-reviews/itme3e94a3f73f71?pid=COMGYSFG7JNFXNM9&lid=LSTCOMGYSFG7JNFXNM9NT4T6Z&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/lenovo-legion-5-intel-core-i7-13th-gen-13650hx-24-gb-512-gb-ssd-windows-11-home-8-graphics-nvidia-geforce-rtx-4060-15irx9-gaming-laptop/product-reviews/itm591a1e64b6eb5?pid=COMH44PGRKK8XHWF&lid=LSTCOMH44PGRKK8XHWFRUZTCO&marketplace=FLIPKART',
    'https://www.flipkart.com/lenovo-legion-5-intel-core-i7-13th-gen-13650hx-24-gb-512-gb-ssd-windows-11-home-8-graphics-nvidia-geforce-rtx-4060-15irx9-gaming-laptop/product-reviews/itm591a1e64b6eb5?pid=COMH44PGRKK8XHWF&lid=LSTCOMH44PGRKK8XHWFRUZTCO&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/apple-macbook-air-m1-8-gb-512-gb-ssd-mac-os-big-sur-z12400092/product-reviews/itmec35accf62a2f?pid=COMG4ZYZMHKH8FEG&lid=LSTCOMG4ZYZMHKH8FEGJFXEEN&marketplace=FLIPKART',
    'https://www.flipkart.com/apple-macbook-air-m1-8-gb-512-gb-ssd-mac-os-big-sur-z12400092/product-reviews/itmec35accf62a2f?pid=COMG4ZYZMHKH8FEG&lid=LSTCOMG4ZYZMHKH8FEGJFXEEN&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/apple-m3-16-gb-256-gb-ssd-macos-sequoia-mc8k4hn-a/product-reviews/itmb1aa0cc739560?pid=COMH64PY8UKCEY9Y&lid=LSTCOMH64PY8UKCEY9YG5NPLS&marketplace=FLIPKART',
    'https://www.flipkart.com/apple-m3-16-gb-256-gb-ssd-macos-sequoia-mc8k4hn-a/product-reviews/itmb1aa0cc739560?pid=COMH64PY8UKCEY9Y&lid=LSTCOMH64PY8UKCEY9YG5NPLS&marketplace=FLIPKART&page=4',
    'https://www.flipkart.com/hp-fc0026au-amd-ryzen-3-quad-core-7320u-8-gb-512-gb-ssd-windows-11-home-15-fc0025au-thin-light-laptop/product-reviews/itm3f21e9fdfc42f?pid=COMGZ7FRZDEQHNYQ&lid=LSTCOMGZ7FRZDEQHNYQRE2P9E&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-fc0026au-amd-ryzen-3-quad-core-7320u-8-gb-512-gb-ssd-windows-11-home-15-fc0025au-thin-light-laptop/product-reviews/itm3f21e9fdfc42f?pid=COMGZ7FRZDEQHNYQ&lid=LSTCOMGZ7FRZDEQHNYQRE2P9E&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/chuwi-intel-core-i3-12th-gen-i3-1215u-12-gb-512-gb-ssd-windows-11-home-freebook-2-1-laptop/product-reviews/itmc5e3f409e7e39?pid=COMGQJZPSGFFF7V7&lid=LSTCOMGQJZPSGFFF7V7T2BU4F&marketplace=FLIPKART',
    'https://www.flipkart.com/chuwi-intel-core-i3-12th-gen-i3-1215u-12-gb-512-gb-ssd-windows-11-home-freebook-2-1-laptop/product-reviews/itmc5e3f409e7e39?pid=COMGQJZPSGFFF7V7&lid=LSTCOMGQJZPSGFFF7V7T2BU4F&marketplace=FLIPKART&page=4',
    'https://www.flipkart.com/avita-liber-e-intel-core-i3-12th-gen-1215u-8-gb-512-gb-ssd-windows-11-home-am15a2int56f-chf-thin-light-laptop/product-reviews/itm7b5db66b53509?pid=COMGZW3N5D29DM5Y&lid=LSTCOMGZW3N5D29DM5YOOJ8JB&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-pavilion-14-touchscreen-intel-core-i5-12th-gen-1235u-16-gb-512-gb-ssd-windows-11-home-14-dv2041tu-laptop/product-reviews/itm5b68c71d614ff?pid=COMGZHNMQFWGTVDX&lid=LSTCOMGZHNMQFWGTVDXHXPDCV&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-vivobook-s14-oled-intel-evo-h-series-core-i5-12th-gen-12500h-16-gb-512-gb-ssd-windows-11-home-s3402za-km501ws-thin-light-laptop/product-reviews/itm635eb6df61d1c?pid=COMGCG2GXUAAMYJF&lid=LSTCOMGCG2GXUAAMYJFOJKKYY&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-vivobook-s14-oled-intel-evo-h-series-core-i5-12th-gen-12500h-16-gb-512-gb-ssd-windows-11-home-s3402za-km501ws-thin-light-laptop/product-reviews/itm635eb6df61d1c?pid=COMGCG2GXUAAMYJF&lid=LSTCOMGCG2GXUAAMYJFOJKKYY&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/asus-tuf-gaming-a15-amd-ryzen-7-octa-core-7435hs-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-fa566ncr-hn054ws-laptop/product-reviews/itma4f834884f6b1?pid=COMH3ZFZSSC85WFC&lid=LSTCOMH3ZFZSSC85WFCCZDNPX&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-tuf-gaming-a15-amd-ryzen-7-octa-core-7435hs-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-fa566ncr-hn054ws-laptop/product-reviews/itma4f834884f6b1?pid=COMH3ZFZSSC85WFC&lid=LSTCOMH3ZFZSSC85WFCCZDNPX&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/lenovo-amd-ryzen-3-quad-core-7330u-8-gb-512-gb-ssd-windows-11-home-tp-e14-gen-5-thin-light-laptop/product-reviews/itmba41ecb80a484?pid=COMHFEJKSZGDHBGB&lid=LSTCOMHFEJKSZGDHBGBEDGWGB&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-one-14-amd-ryzen-3-dual-core-3250u-8-gb-256-gb-ssd-windows-11-home-z2-493-thin-light-laptop/product-reviews/itm283f44123aab0?pid=COMGFHMJFHEDTDD4&lid=LSTCOMGFHMJFHEDTDD49T2ZEE&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-one-14-amd-ryzen-3-dual-core-3250u-8-gb-256-gb-ssd-windows-11-home-z2-493-thin-light-laptop/product-reviews/itm283f44123aab0?pid=COMGFHMJFHEDTDD4&lid=LSTCOMGFHMJFHEDTDD49T2ZEE&marketplace=FLIPKART&page=7',
    'https://www.flipkart.com/infinix-zero-book-ultra-series-laptop-intel-core-i9-12th-gen-12900h-16-gb-512-gb-ssd-windows-11-home-zl12-business/product-reviews/itmad7e026e8b8c5?pid=COMGMFK7B6FTNA4X&lid=LSTCOMGMFK7B6FTNA4XRZ631X&marketplace=FLIPKART',
    'https://www.flipkart.com/msi-katana-17-intel-core-i7-13th-gen-13620h-16-gb-1-tb-ssd-windows-11-home-6-gb-graphics-nvidia-geforce-rtx-4050-144-hz-b13vek-254in-gaming-laptop/product-reviews/itm0fcd6b60bf584?pid=COMGMGSJYJE8PGEA&lid=LSTCOMGMGSJYJE8PGEAWH6QQH&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-tuf-gaming-a15-90whr-battery-amd-ryzen-7-octa-core-7735hs-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-4050-144-hz-140-tgp-fa577nu-lp082w-laptop/product-reviews/itm18565b89ac405?pid=COMGPFPCTS9SK94A&lid=LSTCOMGPFPCTS9SK94AUL5DCS&marketplace=FLIPKART',
    'https://www.flipkart.com/infinix-zerobook-13-intel-core-i7-13th-gen-13700h-16-gb-512-gb-ssd-windows-11-home-zl513-thin-light-laptop/product-reviews/itmad7e026e8b8c5?pid=COMGRFPGDHCJWAMX&lid=LSTCOMGRFPGDHCJWAMXVUROLP&marketplace=FLIPKART',
    'https://www.flipkart.com/infinix-zerobook-13-intel-core-i7-13th-gen-13700h-16-gb-512-gb-ssd-windows-11-home-zl513-thin-light-laptop/product-reviews/itmad7e026e8b8c5?pid=COMGRFPGDHCJWAMX&lid=LSTCOMGRFPGDHCJWAMXVUROLP&marketplace=FLIPKART&page=4',
    'https://www.flipkart.com/infinix-x1-slim-series-intel-core-i3-10th-gen-1005g1-8-gb-256-gb-ssd-windows-11-home-xl21-thin-light-laptop/product-reviews/itm946c99f5a014f?pid=COMGEHP5EFEGWZW5&lid=LSTCOMGEHP5EFEGWZW5AGHTBE&marketplace=FLIPKART',
    'https://www.flipkart.com/infinix-x1-slim-series-intel-core-i3-10th-gen-1005g1-8-gb-256-gb-ssd-windows-11-home-xl21-thin-light-laptop/product-reviews/itm946c99f5a014f?pid=COMGEHP5EFEGWZW5&lid=LSTCOMGEHP5EFEGWZW5AGHTBE&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/asus-vivobook-s-15-oled-intel-core-i9-13th-gen-13900h-16-gb-512-gb-ssd-windows-11-home-s5504va-ma943ws-thin-light-laptop/product-reviews/itm9bb268d9b1aab?pid=COMH3BGBN2AN3TWX&lid=LSTCOMH3BGBN2AN3TWXAFJW5Q&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-intel-core-i5-13th-gen-1334u-16-gb-512-gb-ssd-windows-11-home-15-fd0221tu-thin-light-laptop/product-reviews/itm35a5d83544c54?pid=COMGXNZGBJUZ6B6Z&lid=LSTCOMGXNZGBJUZ6B6ZEIWXKB&marketplace=FLIPKART',
    'https://www.flipkart.com/axl-intel-celeron-dual-core-9th-gen-4-gb-256-gb-ssd-windows-11-home-15w-lap02-thin-light-laptop/product-reviews/itm50377e8d175f3?pid=COMGPXFVFZSH9FYX&lid=LSTCOMGPXFVFZSH9FYXLGV3ST&marketplace=FLIPKART',
    'https://www.flipkart.com/microsoft-laptop-go-3-intel-core-i5-12th-gen-1235u-8-gb-256-gb-ssd-windows-11-home-xk1-00045-thin-light/product-reviews/itm8a768fa3e5823?pid=COMGUSPBNYYPCQKX&lid=LSTCOMGUSPBNYYPCQKXGAWJ22&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-14s-intel-core-i3-11th-gen-8-gb-256-gb-ssd-windows-11-home-14s-dy2500tu-thin-light-laptop/product-reviews/itmd402bd7a16929?pid=COMGYZPAXQRJYJE3&lid=LSTCOMGYZPAXQRJYJE3FWOC67&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-14s-intel-core-i3-11th-gen-8-gb-256-gb-ssd-windows-11-home-14s-dy2500tu-thin-light-laptop/product-reviews/itmd402bd7a16929?pid=COMGYZPAXQRJYJE3&lid=LSTCOMGYZPAXQRJYJE3FWOC67&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/msi-intel-core-i5-12th-gen-12450h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-4050-thin-gf63-12ve-071in-gaming-laptop/product-reviews/itme11f9b16d2c8d?pid=COMGTWHYTHH93XPZ&lid=LSTCOMGTWHYTHH93XPZDFGQVD&marketplace=FLIPKART',
    'https://www.flipkart.com/msi-intel-core-i5-12th-gen-12450h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-4050-thin-gf63-12ve-071in-gaming-laptop/product-reviews/itme11f9b16d2c8d?pid=COMGTWHYTHH93XPZ&lid=LSTCOMGTWHYTHH93XPZDFGQVD&marketplace=FLIPKART&page=3',
    'https://www.flipkart.com/dell-intel-core-i5-11th-gen-8-gb-512-gb-ssd-ubuntu-3420-business-laptop/product-reviews/itmec8d56008358f?pid=COMGN6HRYQKJ9DVD&lid=LSTCOMGN6HRYQKJ9DVDE998XZ&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-intel-core-i3-11th-gen-8-gb-512-gb-ssd-windows-11-home-aspire-lite-al15-51-thin-light-laptop/product-reviews/itm5101dc7b33b19?pid=COMGRWJR46SQNSQX&lid=LSTCOMGRWJR46SQNSQXLCUQQD&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-intel-core-i3-11th-gen-8-gb-512-gb-ssd-windows-11-home-aspire-lite-al15-51-thin-light-laptop/product-reviews/itm5101dc7b33b19?pid=COMGRWJR46SQNSQX&lid=LSTCOMGRWJR46SQNSQXLCUQQD&marketplace=FLIPKART&page=3',
    'https://www.flipkart.com/hp-15s-intel-core-i5-13th-gen-1335u-8-gb-1-tb-ssd-windows-11-home-15-fd0012tu-thin-light-laptop/product-reviews/itmd78475e92c7d9?pid=COMGZVGHVJEMGKZB&lid=LSTCOMGZVGHVJEMGKZBWLGP7R&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-15s-intel-core-i5-13th-gen-1335u-8-gb-1-tb-ssd-windows-11-home-15-fd0012tu-thin-light-laptop/product-reviews/itmd78475e92c7d9?pid=COMGZVGHVJEMGKZB&lid=LSTCOMGZVGHVJEMGKZBWLGP7R&marketplace=FLIPKART&page=4',
    'https://www.flipkart.com/acer-nitro-5-amd-ryzen-hexa-core-7535hs-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-an515-47-gaming-laptop/product-reviews/itm6b6fadc1c8219?pid=COMGZT6ZQBZVEWCW&lid=LSTCOMGZT6ZQBZVEWCWFAKDSH&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-envy13-x360-bf0121tu-intel-core-i5-12th-gen-1230u-16-gb-16-optane-512-ssd-windows-11-home-13-bf0121tu-2-1-laptop/product-reviews/itm7c472a05300e5?pid=COMGH47NWT4HZFYP&lid=LSTCOMGH47NWT4HZFYPJT5O1U&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-envy13-x360-bf0121tu-intel-core-i5-12th-gen-1230u-16-gb-16-optane-512-ssd-windows-11-home-13-bf0121tu-2-1-laptop/product-reviews/itm7c472a05300e5?pid=COMGH47NWT4HZFYP&lid=LSTCOMGH47NWT4HZFYPJT5O1U&marketplace=FLIPKART&page=3',
    'https://www.flipkart.com/infinix-gt-book-intel-core-i5-13th-gen-13420h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-4050-90-w-gl613-gaming-laptop/product-reviews/itme8eb6d660dd4b?pid=COMHYS44GPQTGVH8&lid=LSTCOMHYS44GPQTGVH8TWM2RP&marketplace=FLIPKART',
    'https://www.flipkart.com/avita-liber-e-intel-core-i5-12th-gen-1235u-8-gb-512-gb-ssd-windows-11-home-am14a2inf56f-slf-thin-light-laptop/product-reviews/itmf74daeb866371?pid=COMGZW5BZZR5HPGY&lid=LSTCOMGZW5BZZR5HPGY2MBXNJ&marketplace=FLIPKART',
    'https://www.flipkart.com/dell-intel-core-i5-13th-gen-16-gb-1-tb-ssd-windows-11-home-6-gb-graphics-nvidia-geforce-rtx-3050-g15-5530-gaming-laptop/product-reviews/itme3ae9f2792f1a?pid=COMH3GYMBFZ7QJU7&lid=LSTCOMH3GYMBFZ7QJU7AOAMRD&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-chromebook-intel-celeron-dual-core-n3350-4-gb-64-gb-emmc-storage-chrome-os-c423na-bv0523/product-reviews/itm05555e6f28339?pid=COMG49CZSTYBPQNX&lid=LSTCOMG49CZSTYBPQNX3KHT3H&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-chromebook-intel-celeron-dual-core-n3350-4-gb-64-gb-emmc-storage-chrome-os-c423na-bv0523/product-reviews/itm05555e6f28339?pid=COMG49CZSTYBPQNX&lid=LSTCOMG49CZSTYBPQNX3KHT3H&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/dell-inspiron-5430-intel-core-i5-13th-gen-16-gb-512-gb-ssd-windows-11-home-in54308tr2g001ors1-thin-light-laptop/product-reviews/itm2d84af8f1410c?pid=COMGQ2TVQWSF2S7H&lid=LSTCOMGQ2TVQWSF2S7HPET4NA&marketplace=FLIPKART',
    'https://www.flipkart.com/dell-inspiron-5430-intel-core-i5-13th-gen-16-gb-512-gb-ssd-windows-11-home-in54308tr2g001ors1-thin-light-laptop/product-reviews/itm2d84af8f1410c?pid=COMGQ2TVQWSF2S7H&lid=LSTCOMGQ2TVQWSF2S7HPET4NA&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/dell-intel-core-i3-13th-gen-1305u-8-gb-512-gb-ssd-windows-11-home-vostro-3530-thin-light-laptop/product-reviews/itm79bd3633b64b4?pid=COMGZ8NDUXGPXTVZ&lid=LSTCOMGZ8NDUXGPXTVZDATROE&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-vivobook-15-intel-core-i3-11th-gen-1115g4-8-gb-512-gb-ssd-windows-11-home-x515ea-ej328ws-thin-light-laptop/product-reviews/itmee696f665be05?pid=COMGZKHQQQZBGZZD&lid=LSTCOMGZKHQQQZBGZZDMSPA1H&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-vivobook-15-intel-core-i3-11th-gen-1115g4-8-gb-512-gb-ssd-windows-11-home-x515ea-ej328ws-thin-light-laptop/product-reviews/itmee696f665be05?pid=COMGZKHQQQZBGZZD&lid=LSTCOMGZKHQQQZBGZZDMSPA1H&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/samsung-galaxy-book-2-intel-core-i5-12th-gen-1235u-8-gb-512-gb-ssd-windows-11-home-np550-thin-light-laptop/product-reviews/itmcb89499a3c4e4?pid=COMGH3V3UUGM46BQ&lid=LSTCOMGH3V3UUGM46BQZAGUN0&marketplace=FLIPKART',
    'https://www.flipkart.com/samsung-galaxy-book-2-intel-core-i5-12th-gen-1235u-8-gb-512-gb-ssd-windows-11-home-np550-thin-light-laptop/product-reviews/itmcb89499a3c4e4?pid=COMGH3V3UUGM46BQ&lid=LSTCOMGH3V3UUGM46BQZAGUN0&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/acer-aspire-3-amd-dual-core-3020e-4-gb-256-gb-ssd-windows-11-home-a314-22-laptop/product-reviews/itm3f90aea501859?pid=COMGBNUMF8CDJZFH&lid=LSTCOMGBNUMF8CDJZFHTE1AZY&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-aspire-3-amd-dual-core-3020e-4-gb-256-gb-ssd-windows-11-home-a314-22-laptop/product-reviews/itm3f90aea501859?pid=COMGBNUMF8CDJZFH&lid=LSTCOMGBNUMF8CDJZFHTE1AZY&marketplace=FLIPKART&page=9',
    'https://www.flipkart.com/lenovo-ideapad-gaming-3-amd-ryzen-7-octa-core-r7-5800h-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-15ach6-laptop/product-reviews/itm2a46b1c472cac?pid=COMGGMRSDDRGKFGU&lid=LSTCOMGGMRSDDRGKFGUYCPD5P&marketplace=FLIPKART',
    'https://www.flipkart.com/lenovo-ideapad-gaming-3-amd-ryzen-7-octa-core-r7-5800h-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-15ach6-laptop/product-reviews/itm2a46b1c472cac?pid=COMGGMRSDDRGKFGU&lid=LSTCOMGGMRSDDRGKFGUYCPD5P&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/dell-intel-core-i3-11th-gen-1115g4-8-gb-256-gb-ssd-32-emmc-storage-ubuntu-latitude-3420-business-laptop/product-reviews/itmec8d56008358f?pid=COMGZBHZTTXGGXXZ&lid=LSTCOMGZBHZTTXGGXXZEFGF5P&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-vivobook-s-14-intel-evo-h-series-core-i5-12th-gen-12500h-8-gb-512-gb-ssd-windows-11-home-s3402za-ly522ws-thin-light-laptop/product-reviews/itmfee55947a37e1?pid=COMGNY4VWHZKRSHT&lid=LSTCOMGNY4VWHZKRSHTND9HRE&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-vivobook-s-14-intel-evo-h-series-core-i5-12th-gen-12500h-8-gb-512-gb-ssd-windows-11-home-s3402za-ly522ws-thin-light-laptop/product-reviews/itmfee55947a37e1?pid=COMGNY4VWHZKRSHT&lid=LSTCOMGNY4VWHZKRSHTND9HRE&marketplace=FLIPKART&page=10',
    'https://flipkart.com/lenovo-ideapad-3-intel-core-i3-10th-gen-10110u-8-gb-256-gb-ssd-windows-11-home-15iml05-thin-light-laptop/product-reviews/itm6976e7038f4ba?pid=COMG6AKVAHWTHAQG&lid=LSTCOMG6AKVAHWTHAQG68ORK6&marketplace=FLIPKART',
    'https://flipkart.com/lenovo-ideapad-3-intel-core-i3-10th-gen-10110u-8-gb-256-gb-ssd-windows-11-home-15iml05-thin-light-laptop/product-reviews/itm6976e7038f4ba?pid=COMG6AKVAHWTHAQG&lid=LSTCOMG6AKVAHWTHAQG68ORK6&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/hp-g9-amd-ryzen-3-dual-core-3250u-8-gb-512-gb-ssd-dos-841w6pa-thin-light-laptop/product-reviews/itmffac8a2b263c2?pid=COMGSYYSWMSN2N2Z&lid=LSTCOMGSYYSWMSN2N2ZYSEABY&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-intel-core-i5-11th-gen-8-gb-512-gb-ssd-windows-11-home-al15-51-laptop/product-reviews/itm5101dc7b33b19?pid=COMGS7E7DFZTDW6B&lid=LSTCOMGS7E7DFZTDW6BDZSIOV&marketplace=FLIPKART',
    'https://www.flipkart.com/dell-inspiron-5430-intel-core-i5-13th-gen-16-gb-1-tb-ssd-windows-11-home-in5430jnh1p001ors1-thin-light-laptop/product-reviews/itm2d84af8f1410c?pid=COMGS7Q97SVKWGJJ&lid=LSTCOMGS7Q97SVKWGJJ7N6RRT&marketplace=FLIPKART',
    'https://www.flipkart.com/dell-inspiron-5430-intel-core-i5-13th-gen-16-gb-1-tb-ssd-windows-11-home-in5430jnh1p001ors1-thin-light-laptop/product-reviews/itm2d84af8f1410c?pid=COMGS7Q97SVKWGJJ&lid=LSTCOMGS7Q97SVKWGJJ7N6RRT&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/hp-chromebook-mediatek-mt8183-4-gb-64-gb-emmc-storage-chrome-os-11a-na0002mu/product-reviews/itmd49c881ebf1ac?pid=COMGYJYYA7FFRXZC&lid=LSTCOMGYJYYA7FFRXZCBWFST1&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-chromebook-mediatek-mt8183-4-gb-64-gb-emmc-storage-chrome-os-11a-na0002mu/product-reviews/itmd49c881ebf1ac?pid=COMGYJYYA7FFRXZC&lid=LSTCOMGYJYYA7FFRXZCBWFST1&marketplace=FLIPKART&page=10',
    'https://www.flipkart.com/acer-extensa-15-intel-core-i5-11th-gen-1135g7-8-gb-512-gb-ssd-windows-11-home-ex-215-54-583m-thin-light-laptop/product-reviews/itmb56a6a6028189?pid=COMGGYEBSGX9SEBG&lid=LSTCOMGGYEBSGX9SEBGHRSZVF&marketplace=FLIPKART',
    'https://www.flipkart.com/acer-extensa-15-intel-core-i5-11th-gen-1135g7-8-gb-512-gb-ssd-windows-11-home-ex-215-54-583m-thin-light-laptop/product-reviews/itmb56a6a6028189?pid=COMGGYEBSGX9SEBG&lid=LSTCOMGGYEBSGX9SEBGHRSZVF&marketplace=FLIPKART&page=3',
    'https://www.flipkart.com/asus-vivobook-14-intel-core-i5-13th-gen-1335u-8-gb-512-gb-ssd-windows-11-home-x1404va-nk521ws-thin-light-laptop/product-reviews/itme772f3529c8fc?pid=COMGZDQJAHZJUHNS&lid=LSTCOMGZDQJAHZJUHNSQK20U2&marketplace=FLIPKART',
    'https://www.flipkart.com/asus-vivobook-14-intel-core-i5-13th-gen-1335u-8-gb-512-gb-ssd-windows-11-home-x1404va-nk521ws-thin-light-laptop/product-reviews/itme772f3529c8fc?pid=COMGZDQJAHZJUHNS&lid=LSTCOMGZDQJAHZJUHNSQK20U2&marketplace=FLIPKART&page=2',
    'https://www.flipkart.com/hp-victus-16-intel-core-i5-11th-gen-11400h-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-gtx-1650-144-hz-16-d0311tx-gaming-laptop/product-reviews/itm0d520c75833a9?pid=COMGHYYKESUN5ZKQ&lid=LSTCOMGHYYKESUN5ZKQNTQDKG&marketplace=FLIPKART',
    'https://www.flipkart.com/hp-victus-16-intel-core-i5-11th-gen-11400h-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-gtx-1650-144-hz-16-d0311tx-gaming-laptop/product-reviews/itm0d520c75833a9?pid=COMGHYYKESUN5ZKQ&lid=LSTCOMGHYYKESUN5ZKQNTQDKG&marketplace=FLIPKART&page=8'

]



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

product_data = []

for url in urls:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        # Extracting product details
        title_element = soup.find('div', class_='Vu3-9u eCtPz5')
        title = title_element.get_text(strip=True) if title_element else "N/A"

        nreview_element = soup.find('div', class_='col-4-12 F2+K4v')
        num_reviews = nreview_element.get_text(strip=True) if nreview_element else "N/A"

        authors = [author.get_text(strip=True) for author in soup.find_all('div', class_='row gHqwa8')[:10]]
        ratings = [rating.get_text(strip=True) for rating in soup.find_all('div', class_='XQDdHH Ga3i8K')[:10]]
        review_titles = [rt.get_text(strip=True) for rt in soup.find_all('p', class_='z9E0IG')[:10]]
        review_texts = [review.get_text(strip=True) for review in soup.find_all('div', class_='ZmyHeo')[:10]]

        product_info = {
            "Product URL": url,
            "Title": title,
            "Number of Ratings & Reviews": num_reviews,
            "Authors": ", ".join(authors) if authors else "N/A",
            "Ratings": ", ".join(ratings) if ratings else "N/A",
            "Review Titles": ", ".join(review_titles) if review_titles else "N/A",
            "Review Texts": ", ".join(review_texts) if review_texts else "N/A"
        }

        product_data.append(product_info)

    else:
        print(f"Failed to fetch data from {url}, Status Code: {response.status_code}")

df = pd.DataFrame(product_data)

print(df)

# df.to_csv('flipkart_reviews_laptops.csv', index=False)


