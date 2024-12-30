import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", False) == "True"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
    "mailings",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = os.getenv("USE_I18N", False) == "True"

USE_TZ = os.getenv("USE_TZ", False) == "True"

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", False) == "True"
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", False) == "True"

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
SERVER_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_ADMIN = EMAIL_HOST_USER

AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "mailings:main"
LOGOUT_REDIRECT_URL = "mailings:main"

CACHE_ENABLED = os.getenv("CACHE_ENABLED", False) == "True"
if CACHE_ENABLED:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": os.getenv("LOCATION"),
        }
    }

COUNTRIES = (
    ("AUS", "Австралия"),
    ("AUT", "Австрия"),
    ("AZE", "Азербайджан"),
    ("ALA", "Аландские острова"),
    ("ALB", "Албания"),
    ("DZA", "Алжир"),
    ("VIR", "Виргинские Острова (США)"),
    ("ASM", "Американское Самоа"),
    ("AIA", "Ангилья"),
    ("AGO", "Ангола"),
    ("AND", "Андорра"),
    ("ATA", "Антарктика"),
    ("ATG", "Антигуа и Барбуда"),
    ("ARG", "Аргентина"),
    ("ARM", "Армения"),
    ("ABW", "Аруба"),
    ("AFG", "Афганистан"),
    ("BHS", "Багамские Острова"),
    ("BGD", "Бангладеш"),
    ("BB", "Барбадос"),
    ("BHR", "Бахрейн"),
    ("BLR", "Беларусь"),
    ("BLZ", "Белиз"),
    ("BEL", "Бельгия"),
    ("BEN", "Бенин"),
    ("BMU", "Бермуды"),
    ("BGR", "Болгария"),
    ("BOL", "Боливия"),
    ("BES", "Бонайре, Синт-Эстатиус и Саба"),
    ("BIH", "Босния и Герцеговина"),
    ("BWA", "Ботсвана"),
    ("BRA", "Бразилия"),
    ("IOT", "Британская Территория в Индийском Океане"),
    ("VGB", "Виргинские Острова (Великобритания)"),
    ("BRN", "Бруней"),
    ("BFA", "Буркина-Фасо"),
    ("BDI", "Бурунди"),
    ("BTN", "Бутан"),
    ("VUT", "Вануату"),
    ("VAT", "Ватикан"),
    ("GBR", "Великобритания"),
    ("HUN", "Венгрия"),
    ("VEN", "Венесуэла"),
    ("UMI", "Внешние малые острова США"),
    ("TLS", "Восточный Тимор"),
    ("VNM", "Вьетнам"),
    ("GAB", "Габон"),
    ("HTI", "Гаити"),
    ("GUY", "Гайана"),
    ("GMB", "Гамбия"),
    ("GHA", "Гана"),
    ("GLP", "Гваделупа"),
    ("GTM", "Гватемала"),
    ("GUF", "Гвиана"),
    ("GIN", "Гвинея"),
    ("GNB", "Гвинея-Бисау"),
    ("DEU", "Германия"),
    ("GGY", "Гернси"),
    ("GIB", "Гибралтар"),
    ("HND", "Гондурас"),
    ("HKG", "Гонконг"),
    ("GRD", "Гренада"),
    ("GRL", "Гренландия"),
    ("GRC", "Греция"),
    ("GEO", "Грузия"),
    ("GUM", "Гуам"),
    ("DNK", "Дания"),
    ("JEY", "Джерси"),
    ("DJI", "Джибути"),
    ("DMA", "Доминика"),
    ("DOM", "Доминиканская Республика"),
    ("COD", "ДР Конго"),
    ("EGY", "Египет"),
    ("ZMB", "Замбия"),
    ("ESH", "Западная Сахара"),
    ("ZWE", "Зимбабве"),
    ("ISR", "Израиль"),
    ("IND", "Индия"),
    ("IDN", "Индонезия"),
    ("JOR", "Иордания"),
    ("IRQ", "Ирак"),
    ("IRN", "Иран"),
    ("IRL", "Ирландия"),
    ("ISL", "Исландия"),
    ("ESP", "Испания"),
    ("ITA", "Италия"),
    ("YEM", "Йемен"),
    ("CPV", "Кабо-Верде"),
    ("KAZ", "Казахстан"),
    ("CYM", "Острова Кайман"),
    ("KHM", "Камбоджа"),
    ("CMR", "Камерун"),
    ("CAN", "Канада"),
    ("QAT", "Катар"),
    ("KEN", "Кения"),
    ("CYP", "Кипр"),
    ("KGZ", "Кыргызстан"),
    ("KIR", "Кирибати"),
    ("TWN", "Китайская Республика"),
    ("PRK", "КНДР"),
    ("CHN", "Китай"),
    ("CCK", "Кокосовые острова"),
    ("COL", "Колумбия"),
    ("COM", "Коморские острова"),
    ("CRI", "Коста-Рика"),
    ("CIV", "Кот-д'Ивуар"),
    ("CUB", "Куба"),
    ("KWT", "Кувейт"),
    ("CUW", "Кюрасао"),
    ("LAO", "Лаос"),
    ("LVA", "Латвия"),
    ("LSO", "Лесото"),
    ("LBR", "Либерия"),
    ("LBN", "Ливан"),
    ("LBY", "Ливия"),
    ("LTU", "Литва"),
    ("LIE", "Лихтенштейн"),
    ("LUX", "Люксембург"),
    ("MUS", "Маврикий"),
    ("MRT", "Мавритания"),
    ("MDG", "Мадагаскар"),
    ("MYT", "Майотта"),
    ("MAC", "Макао"),
    ("MKD", "Северная Македония"),
    ("MWI", "Малави"),
    ("MYS", "Малайзия"),
    ("MLI", "Мали"),
    ("MDV", "Мальдивы"),
    ("MLT", "Мальта"),
    ("MAR", "Марокко"),
    ("MTQ", "Мартиника"),
    ("MHL", "Маршалловы острова"),
    ("MEX", "Мексика"),
    ("FSM", "Микронезия"),
    ("MOZ", "Мозамбик"),
    ("MDA", "Молдова"),
    ("MCO", "Монако"),
    ("MNG", "Монголия"),
    ("MSR", "Монтсеррат"),
    ("MMR", "Мьянма"),
    ("NAM", "Намибия"),
    ("NRU", "Науру"),
    ("NPL", "Непал"),
    ("NER", "Нигер"),
    ("NGA", "Нигерия"),
    ("NLD", "Нидерланды"),
    ("NIC", "Никарагуа"),
    ("NIU", "Ниуэ"),
    ("NZL", "Новая Зеландия"),
    ("NCL", "Новая Каледония"),
    ("NOR", "Норвегия"),
    ("ARE", "ОАЭ"),
    ("OMN", "Оман"),
    ("BVT", "Остров Буве"),
    ("IMN", "Остров Мэн"),
    ("COK", "Острова Кука"),
    ("NFK", "Остров Норфолк"),
    ("CXR", "Остров Рождества"),
    ("PCN", "Острова Питкэрн"),
    ("SHN", "Остров Святой Елены"),
    ("PAK", "Пакистан"),
    ("PLW", "Палау"),
    ("PSE", "Государство Палестина"),
    ("PAN", "Панама"),
    ("PNG", "Папуа-Новая Гвинея"),
    ("PRY", "Парагвай"),
    ("PER", "Перу"),
    ("POL", "Польша"),
    ("PRT", "Португалия"),
    ("PRI", "Пуэрто-Рико"),
    ("COG", "Республика Конго"),
    ("KOR", "Республика Корея"),
    ("REU", "Реюньон"),
    ("RUS", "Россия"),
    ("RWA", "Руанда"),
    ("ROU", "Румыния"),
    ("SLV", "Сальвадор"),
    ("WSM", "Самоа"),
    ("SMR", "Сан-Марино"),
    ("STP", "Сан-Томе и Принсипи"),
    ("SAU", "Саудовская Аравия"),
    ("MNP", "Северные Марианские острова"),
    ("SYC", "Сейшельские Острова"),
    ("BLM", "Сен-Бартелеми"),
    ("MAF", "Сен-Мартен"),
    ("SPM", "Сен-Пьер и Микелон"),
    ("SEN", "Сенегал"),
    ("VCT", "Сен-Винсент и Гренадины"),
    ("KNA", "Сент-Китс и Невис"),
    ("LCA", "Сент-Люсия"),
    ("SRB", "Сербия"),
    ("SGP", "Сингапур"),
    ("SXM", "Синт-Мартен"),
    ("SYR", "Сирия"),
    ("SVK", "Словакия"),
    ("SVN", "Словения"),
    ("SLB", "Соломоновы острова"),
    ("SOM", "Сомали"),
    ("SDN", "Судан"),
    ("SUR", "Суринам"),
    ("USA", "США"),
    ("SLE", "Сьерра-Леоне"),
    ("TJK", "Таджикистан"),
    ("THA", "Таиланд"),
    ("TZA", "Танзания"),
    ("TCA", "Теркс и Кайкос"),
    ("TGO", "Того"),
    ("TKL", "Токелау"),
    ("TON", "Тонга"),
    ("TTO", "Тринидад и Тобаго"),
    ("TUV", "Тувалу"),
    ("TUN", "Тунис"),
    ("TKM", "Туркменистан"),
    ("TUR", "Турция"),
    ("UGA", "Уганда"),
    ("UZB", "Узбекистан"),
    ("UKR", "Украина"),
    ("WLF", "Уоллис и Футуна"),
    ("URY", "Уругвай"),
    ("FRO", "Фарерские острова"),
    ("FJI", "Фиджи"),
    ("PHL", "Филиппины"),
    ("FIN", "Финляндия"),
    ("FLK", "Фолклендские острова"),
    ("FRA", "Франция"),
    ("PYF", "Французская Полинезия"),
    ("ATF", "Французские Южные и Антарктические территории"),
    ("HMD", "Херд и Макдональд"),
    ("HRV", "Хорватия"),
    ("CAF", "ЦАР"),
    ("TCD", "Чад"),
    ("MNE", "Черногория"),
    ("CZE", "Чехия"),
    ("CHL", "Чили"),
    ("CHE", "Швейцария"),
    ("SWE", "Швеция"),
    ("SJM", "Шпицберген и Ян-Майен"),
    ("LKA", "Шри-Ланка"),
    ("ECU", "Эквадор"),
    ("GNQ", "Экваториальная Гвинея"),
    ("ERI", "Эритрея"),
    ("SWZ", "Эсватини"),
    ("EST", "Эстония"),
    ("ETH", "Эфиопия"),
    ("ZAF", "ЮАР"),
    ("SGS", "Южная Георгия и Южные Сандвичевы о‐ва"),
    ("SSD", "Южный Судан"),
    ("JAM", "Ямайка"),
    ("JPN", "Япония"),
)

COUNTRY_CODES = (
    ("1", "+1"),
    ("1340", "+1340"),
    ("1649", "+1649"),
    ("20", "+20"),
    ("211", "+211"),
    ("212", "+212"),
    ("213", "+213"),
    ("216", "+216"),
    ("218", "+218"),
    ("220", "+220"),
    ("221", "+221"),
    ("222", "+222"),
    ("223", "+223"),
    ("224", "+224"),
    ("225", "+225"),
    ("226", "+226"),
    ("227", "+227"),
    ("228", "+228"),
    ("229", "+229"),
    ("231", "+231"),
    ("232", "+232"),
    ("233", "+233"),
    ("234", "+234"),
    ("235", "+235"),
    ("236", "+236"),
    ("237", "+237"),
    ("238", "+238"),
    ("239", "+239"),
    ("240", "+240"),
    ("241", "+241"),
    ("242", "+242"),
    ("243", "+243"),
    ("244", "+244"),
    ("245", "+245"),
    ("246", "+246"),
    ("248", "+248"),
    ("249", "+249"),
    ("250", "+250"),
    ("251", "+251"),
    ("252", "+252"),
    ("253", "+253"),
    ("254", "+254"),
    ("255", "+255"),
    ("256", "+256"),
    ("257", "+257"),
    ("258", "+258"),
    ("260", "+260"),
    ("261", "+261"),
    ("262", "+262"),
    ("263", "+263"),
    ("264", "+264"),
    ("265", "+265"),
    ("266", "+266"),
    ("267", "+267"),
    ("268", "+268"),
    ("269", "+269"),
    ("27", "+27"),
    ("290", "+290"),
    ("291", "+291"),
    ("297", "+297"),
    ("298", "+298"),
    ("299", "+299"),
    ("30", "+30"),
    ("31", "+31"),
    ("32", "+32"),
    ("320", "+230"),
    ("33", "+33"),
    ("34", "+34"),
    ("350", "+350"),
    ("351", "+351"),
    ("352", "+352"),
    ("353", "+353"),
    ("354", "+354"),
    ("355", "+355"),
    ("356", "+356"),
    ("357", "+357"),
    ("358", "+358"),
    ("359", "+359"),
    ("36", "+36"),
    ("370", "+370"),
    ("371", "+371"),
    ("372", "+372"),
    ("373", "+373"),
    ("374", "+374"),
    ("375", "+375"),
    ("376", "+376"),
    ("377", "+377"),
    ("378", "+378"),
    ("380", "+380"),
    ("381", "+381"),
    ("382", "+382"),
    ("385", "+385"),
    ("386", "+386"),
    ("387", "+387"),
    ("389", "+389"),
    ("39", "+39"),
    ("40", "+40"),
    ("41", "+41"),
    ("420", "+420"),
    ("421", "+421"),
    ("423", "+423"),
    ("43", "+43"),
    ("44", "+44"),
    ("45", "+45"),
    ("46", "+46"),
    ("47", "+47"),
    ("48", "+48"),
    ("49", "+49"),
    ("500", "+500"),
    ("501", "+501"),
    ("502", "+502"),
    ("503", "+503"),
    ("504", "+504"),
    ("505", "+505"),
    ("506", "+506"),
    ("507", "+507"),
    ("508", "+508"),
    ("509", "+509"),
    ("51", "+51"),
    ("52", "+52"),
    ("53", "+53"),
    ("54", "+54"),
    ("55", "+55"),
    ("56", "+56"),
    ("57", "+57"),
    ("58", "+58"),
    ("590", "+590"),
    ("591", "+591"),
    ("592", "+592"),
    ("593", "+593"),
    ("594", "+594"),
    ("595", "+595"),
    ("596", "+596"),
    ("597", "+597"),
    ("598", "+598"),
    ("599", "+599"),
    ("60", "+60"),
    ("61", "+61"),
    ("62", "+62"),
    ("63", "+63"),
    ("64", "+64"),
    ("65", "+65"),
    ("66", "+66"),
    ("670", "+670"),
    ("672", "+672"),
    ("673", "+673"),
    ("674", "+674"),
    ("675", "+675"),
    ("676", "+676"),
    ("677", "+677"),
    ("678", "+678"),
    ("679", "+679"),
    ("680", "+680"),
    ("681", "+681"),
    ("682", "+682"),
    ("683", "+683"),
    ("685", "+685"),
    ("686", "+686"),
    ("687", "+687"),
    ("688", "+688"),
    ("689", "+689"),
    ("690", "+690"),
    ("691", "+691"),
    ("692", "+692"),
    ("7", "+7"),
    ("81", "+81"),
    ("82", "+82"),
    ("84", "+84"),
    ("850", "+850"),
    ("852", "+852"),
    ("853", "+853"),
    ("855", "+855"),
    ("856", "+856"),
    ("86", "+86"),
    ("880", "+880"),
    ("886", "+886"),
    ("90", "+90"),
    ("91", "+91"),
    ("92", "+92"),
    ("93", "+93"),
    ("94", "+94"),
    ("95", "+95"),
    ("960", "+960"),
    ("961", "+961"),
    ("962", "+962"),
    ("963", "+963"),
    ("964", "+964"),
    ("965", "+965"),
    ("966", "+966"),
    ("967", "+967"),
    ("968", "+968"),
    ("970", "+970"),
    ("971", "+971"),
    ("972", "+972"),
    ("973", "+973"),
    ("974", "+974"),
    ("975", "+975"),
    ("976", "+976"),
    ("977", "+977"),
    ("98", "+98"),
    ("992", "+992"),
    ("993", "+993"),
    ("994", "+994"),
    ("995", "+995"),
    ("996", "+996"),
    ("998", "+998"),
)

MAILING_STATUSES = (
    ("created", "создана"),
    ("started", "запущена"),
    ("finished", "завершена"),
)

ATTEMPT_STATUSES = (
    ("successful", "yспешно"),
    ("unsuccessful", "не yспешно"),
)
