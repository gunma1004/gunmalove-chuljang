import os
from datetime import datetime

BASE_URL = "https://gunmalove-chuljang.netlify.app"
BRAND_NAME = "출장건마사랑"
REP_PHONE = "0507-1280-3344"
TODAY = datetime.today().strftime('%Y-%m-%d')

SHOPS = [
    {"name": "퀸즈홈테라피", "phone": "0507-1280-3296", "score": "4.9", "tags": "맞춤케어 · 타이전문 · 예약금없음"},
    {"name": "오늘밤테라피", "phone": "0507-1280-3199", "score": "4.8", "tags": "이완케어 · 스웨디시 · 후불제"},
    {"name": "주주테라피",   "phone": "0507-1280-3197", "score": "4.8", "tags": "지역맞춤 · 여성전용 · 카드가능"},
    {"name": "한국골든테라피", "phone": "0507-1280-3360", "score": "4.7", "tags": "프리미엄 · 집중케어 · 24시운영"}
]

# 안전한 4대 고급 테마 수식어 순환 설정
SAFE_THEMES = [
    ("출장 맞춤 마사지", "개인별 컨디션과 긴장도에 맞춘 1:1 출장 맞춤 마사지"),
    ("출장 지역맞춤 마사지", "인접 동선 확인으로 빠르게 찾아가는 출장 지역맞춤 마사지"),
    ("출장 이완 마사지", "부드러운 압과 리듬으로 깊은 휴식을 전하는 출장 이완 마사지"),
    ("출장 힐링 마사지", "지친 일상의 피로를 편안히 녹여내는 출장 힐링 마사지")
]

DISTRICTS_DATA = {
    "seoul": [
        ("gangnam-gu", "강남구", [("yeoksam-dong", "역삼동"), ("nonhyeon-dong", "논현동"), ("samsung-dong", "삼성동"), ("daechi-dong", "대치동"), ("sinsa-dong", "신사동"), ("cheongdam-dong", "청담동")]),
        ("seocho-gu", "서초구", [("seocho-dong", "서초동"), ("banpo-dong", "반포동"), ("yangjae-dong", "양재동"), ("bangbae-dong", "방배동"), ("jamwon-dong", "잠원동")]),
        ("songpa-gu", "송파구", [("jamsil-dong", "잠실동"), ("bangi-dong", "방이동"), ("munjeong-dong", "문정동"), ("garak-dong", "가락동"), ("songpa-dong", "송파동")]),
        ("gangdong-gu", "강동구", [("cheonho-dong", "천호동"), ("gildong", "길동"), ("myeongil-dong", "명일동"), ("amsadong", "암사동")]),
        ("mapo-gu", "마포구", [("seogyo-dong", "서교동"), ("hapjeong-dong", "합정동"), ("gongdeok-dong", "공덕동"), ("sangam-dong", "상암동")]),
        ("yeongdeungpo-gu", "영등포구", [("yeouido-dong", "여의도동"), ("dangsan-dong", "당산동"), ("mullae-dong", "문래동"), ("singil-dong", "신길동")]),
        ("gwanak-gu", "관악구", [("sillim-dong", "신림동"), ("bongcheon-dong", "봉천동"), ("nakseongdae-dong", "낙성대동")]),
        ("gangseo-gu", "강서구", [("hwagok-dong", "화곡동"), ("magok-dong", "마곡동"), ("gayang-dong", "가양동"), ("balsan-dong", "발산동")]),
        ("guro-gu", "구로구", [("guro-dong", "구로동"), ("sindorim-dong", "신도림동"), ("gaebong-dong", "개봉동")]),
        ("geumcheon-gu", "금천구", [("gasan-dong", "가산동"), ("doksan-dong", "독산동"), ("siheung-dong", "시흥동")]),
        ("dongjak-gu", "동작구", [("sadang-dong", "사당동"), ("noryangjin-dong", "노량진동"), ("sangdo-dong", "상도동")]),
        ("yongsan-gu", "용산구", [("itaewon-dong", "이태원동"), ("hannam-dong", "한남동"), ("wonhyoro", "원효로"), ("ichon-dong", "이촌동")]),
        ("seongdong-gu", "성동구", [("seongsu-dong", "성수동"), ("haengdang-dong", "행당동"), ("wangsimni", "왕십리")]),
        ("gwangjin-gu", "광진구", [("hwayang-dong", "화양동"), ("guui-dong", "구의동"), ("jayang-dong", "자양동")]),
        ("dongdaemun-gu", "동대문구", [("dapsimni-dong", "답십리동"), ("jangan-dong", "장안동"), ("yongdu-dong", "용두동")]),
        ("jungnang-gu", "중랑구", [("myeonmok-dong", "면목동"), ("sangbong-dong", "상봉동"), ("mukhyeon-dong", "묵동")]),
        ("seongbuk-gu", "성북구", [("gilum-dong", "길음동"), ("donam-dong", "돈암동"), ("seongbuk-dong", "성북동")]),
        ("gangbuk-gu", "강북구", [("mia-dong", "미아동"), ("suyu-dong", "수유동"), ("bun-dong", "번동")]),
        ("dobong-gu", "도봉구", [("chang-dong", "창동"), ("banghak-dong", "방학동"), ("ssangmun-dong", "쌍문동")]),
        ("nowon-gu", "노원구", [("sanggye-dong", "상계동"), ("junggye-dong", "중계동"), ("hagye-dong", "하계동")]),
        ("eunpyeong-gu", "은평구", [("bulgwang-dong", "불광동"), ("galhyeon-dong", "갈현동"), ("eungam-dong", "응암동")]),
        ("seodaemun-gu", "서대문구", [("sinchon-dong", "신촌동"), ("yeonhui-dong", "연희동"), ("hongje-dong", "홍제동")]),
        ("jongno-gu", "종로구", [("jongno-dong", "종로"), ("hyehwa-dong", "혜화동"), ("pyeongchang-dong", "평창동")]),
        ("jung-gu", "중구", [("myeongdong", "명동"), ("euljiro", "을지로"), ("sindang-dong", "신당동")]),
        ("yangcheon-gu", "양천구", [("mok-dong", "목동"), ("sinwol-dong", "신월동"), ("sinjeong-dong", "신정동")])
    ],
    "gyeonggi": [
        ("suwon-si", "수원시", [("ingye-dong", "인계동"), ("maesan-dong", "매산동"), ("yeongtong-dong", "영통동"), ("gwonseon-dong", "권선동"), ("jo-won-dong", "조원동")]),
        ("seongnam-si", "성남시", [("seohyeon-dong", "서현동"), ("jeongja-dong", "정자동"), ("pangyo-dong", "판교동"), ("yataap-dong", "야탑동"), ("moran", "모란")]),
        ("goyang-si", "고양시", [("baekseok-dong", "백석동"), ("madu-dong", "마두동"), ("janghang-dong", "장항동"), ("hwajeong-dong", "화정동"), ("tanhyun-dong", "탄현동")]),
        ("yongin-si", "용인시", [("suji-dong", "수지"), ("jukjeon-dong", "죽전동"), ("giheung-dong", "기흥"), ("dongbaek-dong", "동백동")]),
        ("bucheon-si", "부천시", [("jung-dong", "중동"), ("sang-dong", "상동"), ("sim-gok-dong", "심곡동"), ("songnae-dong", "송내동")]),
        ("ansan-si", "안산시", [("gojan-dong", "고잔동"), ("jungang-dong", "중앙동"), ("seonbu-dong", "선부동"), ("wongok-dong", "원곡동")]),
        ("anyang-si", "안양시", [("beomgye-dong", "범계동"), ("pyeongchon-dong", "평촌동"), ("anyang-dong", "안양동")]),
        ("hwaseong-si", "화성시", [("dongtan-dong", "동탄"), ("byeongjeom-dong", "병점동"), ("hyangnam-eup", "향남")]),
        ("pyeongtaek-si", "평택시", [("sosabeol", "소사벌"), ("seojeong-dong", "서정동"), ("pyeongtaek-dong", "평택동")]),
        ("siheung-si", "시흥시", [("jeongwang-dong", "정왕동"), ("baegot-dong", "배곳동"), ("eun-gye", "은계")]),
        ("gimpo-si", "김포시", [("gurae-dong", "구래동"), ("sau-dong", "사우동"), ("pungmu-dong", "풍무동")]),
        ("paju-si", "파주시", [("yadang-dong", "야당동"), ("geumchon-dong", "금촌동"), ("unjeong", "운정")]),
        ("uijeongbu-si", "의정부시", [("uijeongbu-dong", "의정부동"), ("howon-dong", "호원동"), ("singok-dong", "신곡동")]),
        ("gwangmyeong-si", "광명시", [("cheolsan-dong", "철산동"), ("haan-dong", "하안동"), ("soha-dong", "소하동")]),
        ("hanam-si", "하남시", [("misa-dong", "미사동"), ("sinjang-dong", "신장동"), ("deokpung-dong", "덕풍동")]),
        ("namyangju-si", "남양주시", [("dasang-dong", "다산동"), ("pyeongnae-dong", "평내동"), ("hopyeong-dong", "호평동")]),
        ("gunpo-si", "군포시", [("sanbon-dong", "산본동"), ("dang-dong", "당동")]),
        ("guri-si", "구리시", [("sutaek-dong", "수택동"), ("inmun-dong", "인창동")]),
        ("osan-si", "오산시", [("won-dong", "원동"), ("cheonghak-dong", "청학동")]),
        ("icheon-si", "이천시", [("changjeon-dong", "창전동"), ("jungni-dong", "중리동")])
    ],
    "incheon": [
        ("bupyeong-gu", "부평구", [("bupyeong-dong", "부평동"), ("samsan-dong", "삼산동"), ("cheongcheon-dong", "청천동"), ("sipjeong-dong", "십정동")]),
        ("namdong-gu", "남동구", [("guwol-dong", "구월동"), ("nonhyeon-dong", "논현동"), ("gansuk-dong", "간석동"), ("mansu-dong", "만수동")]),
        ("yeonsu-gu", "연수구", [("songdo-dong", "송도동"), ("yeonsu-dong", "연수동"), ("dongchun-dong", "동춘동"), ("cheonghak-dong", "청학동")]),
        ("michuhol-gu", "미추홀구", [("juan-dong", "주안동"), ("dohwa-dong", "도화동"), ("yonghyeon-dong", "용현동"), ("sungui-dong", "숭의동")]),
        ("seohae-gu", "서구", [("cheongna-dong", "청라동"), ("geomam-dong", "검암동"), ("dangha-dong", "당하동"), ("won-dang-dong", "원당동")]),
        ("gyeyang-gu", "계양구", [("gyesan-dong", "계산동"), ("jakjeon-dong", "작전동"), ("hyoseong-dong", "효성동")]),
        ("jung-gu", "중구", [("unseo-dong", "운서동(영종도)"), ("dongincheon", "동인천"), ("sinpo-dong", "신포동")])
    ]
}

PROV_MAP = {
    "seoul": ("서울특별시", "서울", "/"),
    "gyeonggi": ("경기도", "경기", "/gyeonggi/"),
    "incheon": ("인천광역시", "인천", "/incheon/")
}

def render_shops(loc_title):
    cards = []
    for idx, shop in enumerate(SHOPS, 1):
        clean_phone = shop["phone"].replace("-", "")
        card = f"""          <article class="provider-card">
            <div class="rank">{idx}<small>위</small></div>
            <div class="provider-main">
              <div class="provider-head">
                <h3>{shop['name']}</h3>
                <span>★ {shop['score']}</span>
              </div>
              <div class="tags">
                <span>{shop['tags']}</span>
              </div>
              <p>{loc_title} 전지역 신속 이동 배정. 타이·아로마·스웨디시 안심 후불제 상담을 진행합니다.</p>
              <div class="provider-prices"><span>건식 60분 · 8만</span> / <span>오일 90분 · 11만</span></div>
            </div>
            <a class="provider-phone-btn" href="tel:{clean_phone}">
              <b>전화 상담</b>
              <small>{shop['phone']}</small>
            </a>
          </article>"""
        cards.append(card)
    return "\n".join(cards)

# 1. 서울 메인
def make_main_page(sitemap_list):
    nearby = []
    for d_slug, d_name, d_dongs in DISTRICTS_DATA["seoul"]:
        nearby.append(f'          <a class="region-link" href="/areas/seoul/{d_slug}/"><b>서울 {d_name}</b><span>맞춤 케어 안내</span></a>')
    nearby_html = "\n".join(nearby)

    title_text = f"서울 출장 맞춤 마사지 홈타이 테라피 | 코스 요금표 - {BRAND_NAME}"
    desc_text = f"{BRAND_NAME} 서울 전지역 출장 맞춤 마사지 및 홈타이 스웨디시 안내. 선입금 없는 100% 현장 후불제와 투명한 코스 요금, 각 구·동별 빠른 방문 상담."
    canonical_url = f"{BASE_URL}/"
    sitemap_list.append(canonical_url)

    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
  <title>{title_text}</title>
  <meta name="description" content="{desc_text}">
  <link rel="canonical" href="{canonical_url}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{title_text}">
  <meta property="og:description" content="{desc_text}">
  <meta property="og:url" content="{canonical_url}">

  <link rel="stylesheet" href="/styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "name": "{BRAND_NAME}",
        "url": "{canonical_url}",
        "telephone": "{REP_PHONE}",
        "priceRange": "₩₩",
        "description": "{desc_text}"
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "서울 전지역 동 단위까지 맞춤 방문이 가능한가요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "네, 강남구 역삼동, 서초구 반포동, 송파구 잠실동 등 서울 25개 구 및 세부 동 단위까지 가장 가까운 관리사가 신속 배정됩니다."
            }}
          }},
          {{
            "@type": "Question",
            "name": "선입금이나 예약금이 있나요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "출장건마사랑은 선입금을 일체 받지 않으며, 관리사 도착 후 코스를 확인하고 결제하는 현장 후불제입니다."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body data-page-type="target-home">
  <a class="skip-link" href="#content">본문으로 이동</a>
  
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-text-logo" aria-label="{BRAND_NAME} 홈">
        <span class="brand-badge">건</span>
        <span class="brand-name">출장<span>건마사랑</span></span>
      </a>
      <a class="header-consult" href="#consult">상담 안내</a>
    </div>
  </header>

  <main id="content">
    <section class="home-hero">
      <div class="container">
        <span class="hero-badge">서울 · 경기 · 인천 구·동 단위 출장 맞춤 마사지</span>
        <h1>지친 하루의 피로를<br><em>내 집에서 편안하게 풀어드립니다</em></h1>
        <p>희망 장소(구·동)와 시간, 집중 코스를 알려주시면 당일 최적의 이동 동선으로 빠르게 찾아갑니다.</p>
        <div class="hero-stats">
          <div><b>구·동</b><span>지역맞춤 안내</span></div>
          <div><b>100%</b><span>현장 후불제</span></div>
          <div><b>19~05시</b><span>야간 집중 상담</span></div>
          <div><b>이완</b><span>전신 피로 회복</span></div>
        </div>
        <a class="gold-button" href="#courses">코스와 일정 확인</a>
      </div>
    </section>

    <nav class="province-tabs">
      <div class="container">
        <a href="/" class="active">서울</a>
        <a href="/gyeonggi/">경기</a>
        <a href="/incheon/">인천</a>
      </div>
    </nav>

    <section class="section providers">
      <div class="container">
        <div class="section-row">
          <h2 class="section-title">서울 추천 제휴 매장</h2>
          <span>직통 번호로 빠른 일정 상담</span>
        </div>
        <div class="provider-list">
{render_shops('서울특별시')}
        </div>
      </div>
    </section>

    <section class="section course-section" id="courses">
      <div class="container">
        <h2 class="section-title">서울 코스 &amp; 요금 안내</h2>
        <p class="section-note">상담과 현장에서 시간·범위·비용을 다시 확인하고 선입금 없이 진행합니다.</p>
        <div class="course-grid">
          <article class="course-card"><span class="course-icon">🧘</span><h3>건식 밸런스</h3><p>오일 없이 전신의 뭉친 근육을 부드럽게 이완합니다.</p><div class="price-list"><div class="price-row"><span>60분</span><b>80,000원</b></div><div class="price-row"><span>90분</span><b>100,000원</b></div><div class="price-row"><span>120분</span><b>120,000원</b></div></div></article>
          <article class="course-card"><span class="course-icon">🌿</span><h3>아로마 릴렉스</h3><p>은은한 오일 향과 함께 굳은 몸을 순환시키는 편안한 관리입니다.</p><div class="price-list"><div class="price-row"><span>60분</span><b>90,000원</b></div><div class="price-row"><span>90분</span><b>110,000원</b></div><div class="price-row"><span>120분</span><b>130,000원</b></div></div></article>
          <article class="course-card"><span class="course-icon">💧</span><h3>스웨디시 오일</h3><p>섬세하고 일정한 압으로 전신의 림프와 활력을 깨웁니다.</p><div class="price-list"><div class="price-row"><span>60분</span><b>100,000원</b></div><div class="price-row"><span>90분</span><b>120,000원</b></div><div class="price-row"><span>120분</span><b>140,000원</b></div></div></article>
          <article class="course-card"><span class="course-icon">👑</span><h3>스페셜 VIP</h3><p>전신 집중 관리와 요청 부위를 정밀하게 맞춤 배분합니다.</p><div class="price-list"><div class="price-row"><span>90분</span><b>130,000원</b></div><div class="price-row"><span>120분</span><b>150,000원</b></div></div></article>
          <article class="course-card"><span class="course-icon">✨</span><h3>여성전용 케어</h3><p>프라이빗하고 세심한 배려로 편안하게 진행됩니다.</p><div class="price-list"><div class="price-row"><span>90분</span><b>120,000원</b></div><div class="price-row"><span>120분</span><b>150,000원</b></div><div class="price-row"><span>150분</span><b>180,000원</b></div></div></article>
        </div>
      </div>
    </section>

    <section class="section region-section" id="regions">
      <div class="container">
        <h2 class="section-title">서울 자치구 둘러보기</h2>
        <div class="region-grid">
{nearby_html}
        </div>
      </div>
    </section>

    <section class="section consult" id="consult">
      <div class="container">
        <div class="consult-card">
          <div>
            <b>운영 안내</b>
            <p>선입금을 절대 요구하지 않으며 상단 제휴 매장 번호로 편하게 문의하세요.</p>
          </div>
          <div>
            <b>안심 결제 원칙</b>
            <p>현장에서 관리 범위와 비용을 확인한 후 안심하고 결제합니다.</p>
          </div>
          <a href="tel:{REP_PHONE.replace('-', '')}">대표 상담 전화</a>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-logo-text">출장<span>건마사랑</span></div>
      <p>서울·경기·인천 방문 케어 정보 안내 플랫폼</p>
      <nav>
        <a href="/">서울</a><a href="/gyeonggi/">경기</a><a href="/incheon/">인천</a>
      </nav>
      <small>© 2026 {BRAND_NAME}. All rights reserved.</small>
    </div>
  </footer>

  <a class="fixed-phone-cta" href="tel:{REP_PHONE.replace('-', '')}" aria-label="대표 전화 상담">대표 {REP_PHONE}</a>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

# 2. 광역 허브 (경기, 인천)
def make_hub_page(prov_key, sitemap_list):
    prov_full, prov_short, _ = PROV_MAP[prov_key]
    os.makedirs(prov_key, exist_ok=True)
    canonical_url = f"{BASE_URL}/{prov_key}/"
    sitemap_list.append(canonical_url)

    nearby = []
    for d_slug, d_name, d_dongs in DISTRICTS_DATA[prov_key]:
        nearby.append(f'          <a class="region-link" href="/areas/{prov_key}/{d_slug}/"><b>{d_name}</b><span>맞춤 케어 안내</span></a>')
    nearby_html = "\n".join(nearby)

    theme_word = "출장 지역맞춤 마사지" if prov_key == "gyeonggi" else "출장 이완 마사지"
    title_text = f"{prov_full} {theme_word} 테라피 | 코스 요금표 - {BRAND_NAME}"
    desc_text = f"{BRAND_NAME} {prov_full} 전지역 {theme_word} 안내. 시·군 및 세부 동별 빠른 방문 배정과 선입금 없는 100% 현장 후불제."

    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
  <title>{title_text}</title>
  <meta name="description" content="{desc_text}">
  <link rel="canonical" href="{canonical_url}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{title_text}">
  <meta property="og:description" content="{desc_text}">
  <meta property="og:url" content="{canonical_url}">

  <link rel="stylesheet" href="/styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "name": "{BRAND_NAME} {prov_short}",
        "url": "{canonical_url}",
        "telephone": "{REP_PHONE}",
        "description": "{desc_text}"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }},
          {{ "@type": "ListItem", "position": 2, "name": "{prov_short}", "item": "{canonical_url}" }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body data-page-type="target-province-hub">
  <a class="skip-link" href="#content">본문으로 이동</a>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-text-logo"><span class="brand-badge">건</span><span class="brand-name">출장<span>건마사랑</span></span></a>
      <a class="header-consult" href="#consult">상담 안내</a>
    </div>
  </header>
  <nav class="breadcrumb"><div class="container"><a href="/">홈</a><i>›</i><a href="/{prov_key}/">{prov_short}</a></div></nav>

  <main id="content">
    <section class="directory-head">
      <div class="container">
        <h1>{prov_full} 출장 케어 지역 한눈에</h1>
        <p>{prov_short} 생활권의 출장 맞춤 마사지 구성과 코스, 이용 순서를 한 페이지에서 비교하세요.</p>
        <div class="feature-panels">
          <article><b>🏨 호텔·숙소</b><p>출입 방법과 객실 정보를 미리 확인합니다.</p></article>
          <article><b>🏠 주거 공간</b><p>주차와 공동현관 안내를 함께 전달합니다.</p></article>
          <article><b>📍 생활권 안내</b><p>인접 지역 이동 시간까지 고려합니다.</p></article>
          <article><b>🗓 동별 배정</b><p>세부 동 단위 최적 동선을 확인합니다.</p></article>
        </div>
      </div>
    </section>

    <section class="section providers">
      <div class="container">
        <div class="section-row">
          <h2 class="section-title">{prov_short} 추천 제휴 매장</h2>
          <span>직통 번호로 빠른 배정 상담</span>
        </div>
        <div class="provider-list">
{render_shops(prov_full)}
        </div>
      </div>
    </section>

    <section class="section region-section">
      <div class="container">
        <h2 class="section-title">{prov_short} 세부 지역 안내</h2>
        <div class="region-grid">
{nearby_html}
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-logo-text">출장<span>건마사랑</span></div>
      <p>{prov_full} 방문 케어 정보 플랫폼</p>
      <small>© 2026 {BRAND_NAME}. All rights reserved.</small>
    </div>
  </footer>
  <a class="fixed-phone-cta" href="tel:{REP_PHONE.replace('-', '')}">대표 {REP_PHONE}</a>
</body>
</html>"""
    with open(os.path.join(prov_key, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

# 3. 구/시 단위 및 세부 '동' 단위 페이지 자동 생성
def make_area_and_dong_pages(sitemap_list):
    district_count = 0
    dong_count = 0
    theme_idx = 0

    for prov_key, dist_list in DISTRICTS_DATA.items():
        prov_full, prov_short, prov_hub_url = PROV_MAP[prov_key]

        for d_slug, d_name, dongs in dist_list:
            # (1) 구/시/군 페이지 생성
            dist_dir = os.path.join("areas", prov_key, d_slug)
            os.makedirs(dist_dir, exist_ok=True)
            dist_canonical = f"{BASE_URL}/areas/{prov_key}/{d_slug}/"
            sitemap_list.append(dist_canonical)

            dong_links = []
            for dong_slug, dong_name in dongs:
                dong_links.append(f'          <a class="region-link" href="/areas/{prov_key}/{d_slug}/{dong_slug}/"><b>{dong_name}</b><span>맞춤 케어 안내</span></a>')
            dong_links_html = "\n".join(dong_links)

            # 구 단위 테마 타이틀
            cur_theme, cur_theme_desc = SAFE_THEMES[theme_idx % len(SAFE_THEMES)]
            theme_idx += 1

            dist_title = f"{prov_short} {d_name} {cur_theme} 홈타이 | {BRAND_NAME}"
            dist_desc = f"{BRAND_NAME} {prov_short} {d_name} 전지역 및 세부 동별 안내. {cur_theme_desc}와 선입금 없는 100% 현장 후불제."

            dist_html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
  <title>{dist_title}</title>
  <meta name="description" content="{dist_desc}">
  <link rel="canonical" href="{dist_canonical}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{dist_title}">
  <meta property="og:description" content="{dist_desc}">
  <meta property="og:url" content="{dist_canonical}">

  <link rel="stylesheet" href="/styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "name": "{BRAND_NAME} {d_name}",
        "url": "{dist_canonical}",
        "telephone": "{REP_PHONE}",
        "description": "{dist_desc}"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }},
          {{ "@type": "ListItem", "position": 2, "name": "{prov_short}", "item": "{prov_hub_url}" }},
          {{ "@type": "ListItem", "position": 3, "name": "{d_name}", "item": "{dist_canonical}" }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body data-page-type="target-district-hub">
  <a class="skip-link" href="#content">본문으로 이동</a>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-text-logo"><span class="brand-badge">건</span><span class="brand-name">출장<span>건마사랑</span></span></a>
      <a class="header-consult" href="#consult">상담 안내</a>
    </div>
  </header>
  <nav class="breadcrumb"><div class="container"><a href="/">홈</a><i>›</i><a href="{prov_hub_url}">{prov_short}</a><i>›</i><a href="{dist_canonical}">{d_name}</a></div></nav>

  <main id="content">
    <section class="directory-head">
      <div class="container">
        <h1>{prov_full} {d_name} 출장 케어 한눈에</h1>
        <p>{d_name} 전지역 및 세부 동별 신속 방문이 가능한 4대 전문 업체를 안내합니다.</p>
        <div class="filter-pills"><span>스웨디시</span><span>아로마</span><span>타이</span><span>여성전용</span></div>
      </div>
    </section>

    <section class="section providers">
      <div class="container">
        <div class="section-row">
          <h2 class="section-title">{d_name} 추천 제휴 매장</h2>
          <span>희망 매장 직통 번호로 빠른 배정</span>
        </div>
        <div class="provider-list">
{render_shops(d_name)}
        </div>
      </div>
    </section>

    <section class="section region-section">
      <div class="container">
        <h2 class="section-title">{d_name} 세부 동별 바로가기</h2>
        <div class="region-grid">
{dong_links_html}
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-logo-text">출장<span>건마사랑</span></div>
      <p>{d_name} 출장 케어 예약 및 코스 상담</p>
      <small>© 2026 {BRAND_NAME}. All rights reserved.</small>
    </div>
  </footer>
  <a class="fixed-phone-cta" href="tel:{REP_PHONE.replace('-', '')}">대표 {REP_PHONE}</a>
</body>
</html>"""
            with open(os.path.join(dist_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(dist_html)
            district_count += 1

            # (2) 세부 '동' 페이지 생성
            for dong_slug, dong_name in dongs:
                dong_dir = os.path.join(dist_dir, dong_slug)
                os.makedirs(dong_dir, exist_ok=True)
                dong_canonical = f"{BASE_URL}/areas/{prov_key}/{d_slug}/{dong_slug}/"
                sitemap_list.append(dong_canonical)

                # 동 단위 테마 순환 (맞춤 마사지 / 지역맞춤 마사지 / 이완 마사지 / 힐링 마사지)
                dong_theme, dong_theme_desc = SAFE_THEMES[theme_idx % len(SAFE_THEMES)]
                theme_idx += 1

                dong_title = f"{d_name} {dong_name} {dong_theme} 홈타이 테라피 | {BRAND_NAME}"
                dong_desc = f"{BRAND_NAME} {d_name} {dong_name} 방문 안내. {dong_theme_desc}와 선입금 없는 100% 현장 후불제 직통 예약."

                dong_html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
  <title>{dong_title}</title>
  <meta name="description" content="{dong_desc}">
  <link rel="canonical" href="{dong_canonical}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{dong_title}">
  <meta property="og:description" content="{dong_desc}">
  <meta property="og:url" content="{dong_canonical}">

  <link rel="stylesheet" href="/styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "name": "{BRAND_NAME} {dong_name}",
        "url": "{dong_canonical}",
        "telephone": "{REP_PHONE}",
        "priceRange": "₩₩",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "{dong_name}",
          "addressRegion": "{d_name}",
          "addressCountry": "KR"
        }},
        "description": "{dong_desc}"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }},
          {{ "@type": "ListItem", "position": 2, "name": "{prov_short}", "item": "{prov_hub_url}" }},
          {{ "@type": "ListItem", "position": 3, "name": "{d_name}", "item": "{dist_canonical}" }},
          {{ "@type": "ListItem", "position": 4, "name": "{dong_name}", "item": "{dong_canonical}" }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "{dong_name} 방문 시 추가 출장비가 발생하나요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "표기된 코스 비용 외에 별도의 부당한 추가 요금을 요구하지 않으며, 현장에서 범위를 다시 확인합니다."
            }}
          }},
          {{
            "@type": "Question",
            "name": "예약금 없이 이용할 수 있나요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{dong_name} 지역 역시 100% 현장 후불제로 운영되며 선입금을 절대 요구하지 않습니다."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body data-page-type="target-dong-hub">
  <a class="skip-link" href="#content">본문으로 이동</a>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-text-logo"><span class="brand-badge">건</span><span class="brand-name">출장<span>건마사랑</span></span></a>
      <a class="header-consult" href="#consult">상담 안내</a>
    </div>
  </header>
  <nav class="breadcrumb"><div class="container"><a href="/">홈</a><i>›</i><a href="{prov_hub_url}">{prov_short}</a><i>›</i><a href="{dist_canonical}">{d_name}</a><i>›</i><a href="{dong_canonical}">{dong_name}</a></div></nav>

  <main id="content">
    <section class="directory-head">
      <div class="container">
        <h1>{d_name} {dong_name} 출장 케어 안내</h1>
        <p>{dong_name} 일대에서 가장 빠른 이동 동선 배정이 가능한 4대 제휴 업체를 안내합니다.</p>
        <div class="filter-pills"><span>스웨디시</span><span>아로마</span><span>타이</span><span>여성전용</span></div>
      </div>
    </section>

    <section class="section providers">
      <div class="container">
        <div class="section-row">
          <h2 class="section-title">{dong_name} 직통 상담 추천 업체</h2>
          <span>선입금 없는 안심 후불제 상담</span>
        </div>
        <div class="provider-list">
{render_shops(f"{d_name} {dong_name}")}
        </div>
      </div>
    </section>

    <section class="section region-section">
      <div class="container">
        <h2 class="section-title">{d_name} 인근 동 둘러보기</h2>
        <div class="region-grid">
{dong_links_html}
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-logo-text">출장<span>건마사랑</span></div>
      <p>{d_name} {dong_name} 출장 케어 예약 안내</p>
      <small>© 2026 {BRAND_NAME}. All rights reserved.</small>
    </div>
  </footer>
  <a class="fixed-phone-cta" href="tel:{REP_PHONE.replace('-', '')}">대표 {REP_PHONE}</a>
</body>
</html>"""
                with open(os.path.join(dong_dir, "index.html"), "w", encoding="utf-8") as f:
                    f.write(dong_html)
                dong_count += 1

    return district_count, dong_count

def run():
    print(f"[{BRAND_NAME}] 안전 맞춤/지역맞춤/이완 키워드 적용 빌드를 시작합니다...")
    sitemap_list = []
    
    make_main_page(sitemap_list)
    make_hub_page("gyeonggi", sitemap_list)
    make_hub_page("incheon", sitemap_list)
    d_cnt, dong_cnt = make_area_and_dong_pages(sitemap_list)

    xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in sitemap_list:
        xml_lines.append('<url>')
        xml_lines.append(f'<loc>{u}</loc>')
        xml_lines.append('</url>')
    xml_lines.append('</urlset>')

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))

    print(f"빌드 완료! 총 {len(sitemap_list)}개 URL(구 {d_cnt}개, 동 {dong_cnt}개)의 타이틀이 '맞춤/지역맞춤/이완' 키워드로 업데이트되었습니다.")

if __name__ == "__main__":
    run()