

## معرفی
این اسکریپت به‌طور سیستماتیک تنظیمات Vmess، Vless، ShadowSocks، Trojan، Reality، Hysteria، Tuic و Juicity را از کانال‌های تلگرام عمومی جمع‌آوری می‌کند. این تنظیمات بر اساس پورت‌های باز و بسته دسته‌بندی می‌شوند، ورودی‌های تکراری حذف می‌شوند، آدرس‌های پیکربندی با استفاده از آدرس‌های IP حل می‌شوند، و عناوین پیکربندی به‌گونه‌ای اصلاح می‌شوند که ویژگی‌های سرور و نوع پروتکل را نمایش دهند. این ویژگی‌ها شامل نوع شبکه و امنیت، آدرس IP و پورت، و کشور مربوط به پیکربندی می‌باشند.

![آخرین تغییرات در گیت‌هاب](https://img.shields.io/github/last-commit/Amirwopi/Wopi-Config?label=Last%20Commit&color=%2338914b)
![گواهی‌نامه گیت‌هاب](https://img.shields.io/github/license/Amirwopi/Wopi-Config?label=License&color=yellow)
![ستاره‌های گیت‌هاب](https://img.shields.io/github/stars/Amirwopi/Wopi-Config?label=Stars&color=red&style=flat)
![فورک‌های گیت‌هاب](https://img.shields.io/github/forks/Amirwopi/Wopi-Config?label=Forks&color=blue&style=flat)
[![Set up App Runner](https://github.com/Amirwopi/Wopi-Config/actions/workflows/schedule.yml/badge.svg)](https://github.com/Amirwopi/Wopi-Config/actions/workflows/schedule.yml)




## آموزش
لیست دامنه‌ها برای عبور از فیلتر، مسدودسازی و پروکسی کردن بر اساس موقعیت جغرافیایی `ir` در `nekoray` و `nekobox` تنظیم شده است و به هسته `sing-box` وابسته است. برای تنظیم این دامنه‌ها، مسیرهای جدیدی در `nekobox` و `nekoray` ایجاد کرده و دامنه‌های زیر را در بخش مربوط به `domains` وارد کنید. مقدار خروجی را به `bypass`، `proxy` یا `block` بر اساس مشخصات تعیین‌شده تنظیم کنید.

### بای پس
```
geosite:category-bank-ir
geosite:category-bourse-ir
geosite:category-education-ir
geosite:category-forums-ir
geosite:category-gov-ir
geosite:category-insurance-ir
geosite:category-media-ir
geosite:category-news-ir
geosite:category-payment-ir
geosite:category-scholar-ir
geosite:category-shopping-ir
geosite:category-social-media-ir
geosite:category-tech-ir
geosite:category-travel-ir
```

### پروکسی
```
geosite:apple
geosite:adobe
geosite:anthropic
geosite:openai
geosite:clubhouse
geosite:netflix
geosite:nvidia
geosite:intel
geosite:amd
geosite:signal
geosite:soundcloud
geosite:youtube
geosite:telegram
geosite:twitter
geosite:instagram
geosite:facebook
geosite:whatsapp
geosite:pinterest
geosite:tiktok
geosite:spotify
geosite:twitch
geosite:discord
```

### مسدودسازی
```
geosite:category-ads-all
geosite:category-ads-ir
geosite:google-ads
geosite:spotify-ads
geosite:adobe-ads
geosite:apple-ads
```

## لینک‌های اشتراک‌گذاری نوع پروتکل
لینک‌های اشتراک‌گذاری پیکربندی‌ها بر اساس نوع پروتکل و تفکیک شده به کانال‌های تلگرام و لینک‌های اشتراک‌گذاری:

| **نوع پروتکل** | **پیکربندی‌های ترکیبی** | **کانال‌های تلگرام** | **لینک‌های اشتراک‌گذاری** |
|:---:|:---:|:---:|:---:|
| **پیکربندی‌های Juicity** | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/protocols/juicity) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/protocols/juicity) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/protocols/juicity) |
| **پیکربندی‌های Hysteria** | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/protocols/hysteria) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/protocols/hysteria) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/protocols/hysteria) |
| **پیکربندی‌های Tuic** | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/protocols/tuic) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/protocols/tuic) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/protocols/tuic) |
| **پیکربندی‌های Reality** | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/protocols/reality) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/protocols/reality) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/protocols/reality) |
| **پیکربندی‌های Vless** | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/protocols/vless) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/protocols/vless) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/protocols/vless) |
| **پیکربندی‌های Vmess** | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/protocols/vmess) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/protocols/vmess) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/protocols/vmess) |
| **پیکربندی‌های Trojan** | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/protocols/trojan) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/protocols/trojan) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/protocols/trojan) |
| **پیکربندی‌های Shadowsocks** | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/protocols/shadowsocks) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/protocols/shadowsocks) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/protocols/shadowsocks) |
| **پیکربندی‌های تست شده جدید !!** | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/encoded_valid_configs) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/encoded_valid_configs) | [لینک اشتراک‌گذاری](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/encoded_valid_configs) |

## لینک‌های اشتراک نوع شبکه
لینک‌های اشتراک پیکربندی‌ها بر اساس نوع شبکه و جدا شده به کانال‌های تلگرام و لینک‌های اشتراک:

| **نوع شبکه** | **پیکربندی‌های ترکیبی** | **کانال‌های تلگرام** | **لینک‌های اشتراک** |
|:---:|:---:|:---:|:---:|
| **Google Remote Procedure Call (GRPC)** | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/networks/grpc) | [لینک اشتراک کانال](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/networks/grpc) | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/networks/grpc) |
| **Hypertext Transfer Protocol (HTTP)** | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/networks/http) | [لینک اشتراک کانال](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/networks/http) | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/networks/http) |
| **WebSocket Protocol (WS)** | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/networks/ws) | [لینک اشتراک کانال](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/networks/ws) | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/networks/ws) |
| **Transmission Control Protocol (TCP)** | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/networks/tcp) | [لینک اشتراک کانال](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/networks/tcp) | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/networks/tcp) |

## لینک‌های اشتراک نوع امنیت
لینک‌های اشتراک پیکربندی‌ها بر اساس نوع امنیت و جدا شده به کانال‌های تلگرام و لینک‌های اشتراک:

| **نوع امنیت** | **پیکربندی‌های ترکیبی** | **کانال‌های تلگرام** | **لینک‌های اشتراک** |
|:---:|:---:|:---:|:---:|
| **Transport Layer Security (TLS)** | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/security/tls) | [لینک اشتراک کانال](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/security/tls) | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/security/tls) |
| **Non Transport Layer Security (Non-TLS)** | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/security/non-tls) | [لینک اشتراک کانال](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/security/non-tls) | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/security/non-tls) |

## لینک‌های اشتراک نوع پروتکل اینترنت
لینک‌های اشتراک پیکربندی‌ها بر اساس نوع پروتکل اینترنت و جدا شده به کانال‌های تلگرام و لینک‌های اشتراک:

| **نوع پروتکل اینترنت** | **پیکربندی‌های ترکیبی** | **کانال‌های تلگرام** | **لینک‌های اشتراک** |
|:---:|:---:|:---:|:---:|
| **Internet Protocol Version 4 (IPV4)** | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/layers/ipv4) | [لینک اشتراک کانال](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/layers/ipv4) | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/layers/ipv4) |
| **Internet Protocol Version 6 (IPV6)** | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/layers/ipv6) | [لینک اشتراک کانال](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/channels/layers/ipv6) | [لینک اشتراک](https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/subscribe/layers/ipv6) |

## لینک‌های اشتراک بر اساس کشور
لینک‌های اشتراک پیکربندی‌ها بر اساس کشور برای خدماتی که ممکن است منجر به مسدود شدن حساب‌ها شوند، مانند رسانه‌های اجتماعی و خدمات هوش مصنوعی:

| **Code** | **Country Name** | **Subscription Link** | **Code** | **Country Name** | **Subscription Link** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| AL | Albania | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/al/mixed) | AM | Armenia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/am/mixed) |
| AU | Australia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/au/mixed) | AT | Austria | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/at/mixed) |
| BH | Bahrain | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bh/mixed) | BD | Bangladesh | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bd/mixed) |
| BE | Belgium | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/be/mixed) | BZ | Belize | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bz/mixed) |
| BO | Bolivia, Plurinational State of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bo/mixed) | BA | Bosnia and Herzegovina | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ba/mixed) |
| BR | Brazil | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/br/mixed) | BG | Bulgaria | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bg/mixed) |
| CA | Canada | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ca/mixed) | CN | China | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cn/mixed) |
| CO | Colombia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/co/mixed) | CR | Costa Rica | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cr/mixed) |
| HR | Croatia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/hr/mixed) | CY | Cyprus | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cy/mixed) |
| CZ | Czechia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cz/mixed) | DK | Denmark | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/dk/mixed) |
| EC | Ecuador | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ec/mixed) | EE | Estonia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ee/mixed) |
| FI | Finland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/fi/mixed) | FR | France | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/fr/mixed) |
| DE | Germany | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/de/mixed) | GR | Greece | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gr/mixed) |
| HK | Hong Kong | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/hk/mixed) | HU | Hungary | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/hu/mixed) |
| IS | Iceland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/is/mixed) | IN | India | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/in/mixed) |
| IR | Iran, Islamic Republic of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ir/mixed) | IE | Ireland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ie/mixed) |
| IL | Israel | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/il/mixed) | IT | Italy | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/it/mixed) |
| JP | Japan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/jp/mixed) | JO | Jordan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/jo/mixed) |
| KZ | Kazakhstan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/kz/mixed) | KE | Kenya | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ke/mixed) |
| KR | Korea, Republic of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/kr/mixed) | KW | Kuwait | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/kw/mixed) |
| LV | Latvia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/lv/mixed) | LT | Lithuania | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/lt/mixed) |
| LU | Luxembourg | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/lu/mixed) | MO | Macao | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mo/mixed) |
| MT | Malta | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mt/mixed) | MX | Mexico | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mx/mixed) |
| MD | Moldova, Republic of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/md/mixed) | MA | Morocco | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ma/mixed) |
| NL | Netherlands | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/nl/mixed) | NG | Nigeria | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ng/mixed) |
| MK | North Macedonia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mk/mixed) | NO | Norway | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/no/mixed) |
| NA | Not Available | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/na/mixed) | PA | Panama | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pa/mixed) |
| PY | Paraguay | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/py/mixed) | PL | Poland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pl/mixed) |
| PR | Puerto Rico | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pr/mixed) | RO | Romania | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ro/mixed) |
| RU | Russian Federation | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ru/mixed) | SA | Saudi Arabia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sa/mixed) |
| RS | Serbia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/rs/mixed) | SC | Seychelles | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sc/mixed) |
| SG | Singapore | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sg/mixed) | SI | Slovenia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/si/mixed) |
| ES | Spain | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/es/mixed) | SE | Sweden | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/se/mixed) |
| CH | Switzerland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ch/mixed) | TW | Taiwan, Province of China | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/tw/mixed) |
| TR | Türkiye | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/tr/mixed) | UA | Ukraine | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ua/mixed) |
| AE | United Arab Emirates | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ae/mixed) | GB | United Kingdom | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gb/mixed) |
| US | United States | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/us/mixed) | UY | Uruguay | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/uy/mixed) |
| VN | Viet Nam | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/vn/mixed) | VG | Virgin Islands, British | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/vg/mixed) |

| **Code** | **Country Name** | **Subscription Link** | **Code** | **Country Name** | **Subscription Link** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| AL | Albania | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/al/mixed) | AR | Argentina | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ar/mixed) |
| AM | Armenia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/am/mixed) | AU | Australia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/au/mixed) |
| AT | Austria | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/at/mixed) | AZ | Azerbaijan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/az/mixed) |
| BH | Bahrain | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bh/mixed) | BD | Bangladesh | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bd/mixed) |
| BY | Belarus | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/by/mixed) | BE | Belgium | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/be/mixed) |
| BZ | Belize | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bz/mixed) | BO | Bolivia, Plurinational State of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bo/mixed) |
| BA | Bosnia and Herzegovina | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ba/mixed) | BR | Brazil | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/br/mixed) |
| BG | Bulgaria | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/bg/mixed) | KH | Cambodia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/kh/mixed) |
| CA | Canada | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ca/mixed) | CL | Chile | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cl/mixed) |
| CN | China | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cn/mixed) | CO | Colombia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/co/mixed) |
| CR | Costa Rica | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cr/mixed) | HR | Croatia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/hr/mixed) |
| CY | Cyprus | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cy/mixed) | CZ | Czechia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/cz/mixed) |
| DK | Denmark | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/dk/mixed) | EC | Ecuador | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ec/mixed) |
| EE | Estonia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ee/mixed) | FI | Finland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/fi/mixed) |
| FR | France | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/fr/mixed) | GE | Georgia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ge/mixed) |
| DE | Germany | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/de/mixed) | GI | Gibraltar | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gi/mixed) |
| GR | Greece | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gr/mixed) | GT | Guatemala | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gt/mixed) |
| HK | Hong Kong | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/hk/mixed) | HU | Hungary | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/hu/mixed) |
| IS | Iceland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/is/mixed) | IN | India | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/in/mixed) |
| ID | Indonesia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/id/mixed) | IR | Iran, Islamic Republic of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ir/mixed) |
| IQ | Iraq | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/iq/mixed) | IE | Ireland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ie/mixed) |
| IL | Israel | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/il/mixed) | IT | Italy | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/it/mixed) |
| JP | Japan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/jp/mixed) | JO | Jordan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/jo/mixed) |
| KZ | Kazakhstan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/kz/mixed) | KE | Kenya | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ke/mixed) |
| KR | Korea, Republic of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/kr/mixed) | KW | Kuwait | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/kw/mixed) |
| LV | Latvia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/lv/mixed) | LT | Lithuania | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/lt/mixed) |
| LU | Luxembourg | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/lu/mixed) | MO | Macao | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mo/mixed) |
| MY | Malaysia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/my/mixed) | MT | Malta | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mt/mixed) |
| MU | Mauritius | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mu/mixed) | MX | Mexico | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mx/mixed) |
| MD | Moldova, Republic of | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/md/mixed) | MA | Morocco | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ma/mixed) |
| NP | Nepal | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/np/mixed) | NL | Netherlands | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/nl/mixed) |
| NZ | New Zealand | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/nz/mixed) | NG | Nigeria | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ng/mixed) |
| MK | North Macedonia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/mk/mixed) | NO | Norway | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/no/mixed) |
| NA | Not Available | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/na/mixed) | OM | Oman | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/om/mixed) |
| PK | Pakistan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pk/mixed) | PA | Panama | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pa/mixed) |
| PY | Paraguay | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/py/mixed) | PE | Peru | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pe/mixed) |
| PH | Philippines | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ph/mixed) | PL | Poland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pl/mixed) |
| PT | Portugal | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pt/mixed) | PR | Puerto Rico | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/pr/mixed) |
| RO | Romania | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ro/mixed) | RU | Russian Federation | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ru/mixed) |
| SA | Saudi Arabia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sa/mixed) | RS | Serbia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/rs/mixed) |
| SC | Seychelles | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sc/mixed) | SG | Singapore | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sg/mixed) |
| SK | Slovakia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/sk/mixed) | SI | Slovenia | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/si/mixed) |
| ZA | South Africa | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/za/mixed) | ES | Spain | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/es/mixed) |
| SE | Sweden | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/se/mixed) | CH | Switzerland | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ch/mixed) |
| TW | Taiwan, Province of China | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/tw/mixed) | TH | Thailand | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/th/mixed) |
| TR | Türkiye | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/tr/mixed) | UA | Ukraine | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ua/mixed) |
| AE | United Arab Emirates | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ae/mixed) | GB | United Kingdom | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/gb/mixed) |
| US | United States | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/us/mixed) | UY | Uruguay | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/uy/mixed) |
| UZ | Uzbekistan | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/uz/mixed) | VN | Viet Nam | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/vn/mixed) |
| VG | Virgin Islands, British | [Subscription Link](https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/vg/mixed) |
## Stats
[![Stars](https://starchart.cc/Amirwopi/Wopi-Config.svg?variant=adaptive)](https://starchart.cc/Amirwopi/Wopi-Config)
## Activity
![Alt](https://repobeats.axiom.co/api/embed/dbdd0aa054f970fddc69bcd148118fdaa160c088.svg "Repobeats analytics image")
