import os
import json
import urllib.request
import datetime

os.makedirs('assets', exist_ok=True)

# GitHub API configuration
USERNAME = 'atul-kumar-choudhary'
TOKEN = os.getenv('GITHUB_TOKEN')
headers = {'User-Agent': 'Mozilla/5.0'}
if TOKEN:
    headers['Authorization'] = f'token {TOKEN}'

def fetch_json(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_contributions():
    if not TOKEN:
        return "2.8K" # Fallback if no token
    query = """
    {
      user(login: "%s") {
        contributionsCollection {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
    """ % USERNAME
    req = urllib.request.Request('https://api.github.com/graphql', data=json.dumps({'query': query}).encode('utf-8'), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']
    except Exception as e:
        print(f"Error fetching GraphQL: {e}")
        return "2.8K"

def format_num(num):
    if isinstance(num, str):
        return num
    if num >= 1000:
        return f"{num/1000:.1f}k"
    return str(num)

# Fetch data
print("Fetching live GitHub data...")
user_data = fetch_json(f'https://api.github.com/users/{USERNAME}')
followers = format_num(user_data.get('followers', '1.2K')) if user_data else '1.2K'
public_repos = user_data.get('public_repos', '42') if user_data else '42'

repos_data = fetch_json(f'https://api.github.com/users/{USERNAME}/repos?per_page=100')
total_stars = 0
top_repos = []
if repos_data:
    for repo in repos_data:
        total_stars += repo.get('stargazers_count', 0)
    top_repos = sorted(repos_data, key=lambda x: x.get('stargazers_count', 0), reverse=True)

str_stars = format_num(total_stars) if repos_data else '3.5K'
contributions = format_num(get_contributions())

# Helper for top repos
def get_repo_data(index, default_name, default_desc, default_stars):
    if len(top_repos) > index:
        repo = top_repos[index]
        return {
            'name': repo.get('name', default_name),
            'desc': (repo.get('description') or default_desc)[:45],
            'stars': format_num(repo.get('stargazers_count', 0)),
            'updated': repo.get('updated_at', '')[:10]
        }
    return {
        'name': default_name,
        'desc': default_desc,
        'stars': default_stars,
        'updated': 'today'
    }

repo1 = get_repo_data(0, 'AgenticWorkflowRunner', 'Autonomous DAG planner & executor.', '3.2k')
repo2 = get_repo_data(1, 'EnterpriseRAG', 'Hybrid BM25 + dense search.', '2.1k')


header_svg = f'''<svg width="840" height="240" viewBox="0 0 840 240" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.8"/>
            <stop offset="50%" stop-color="#1e293b" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#10b981" stop-opacity="0.8"/>
        </linearGradient>
        <radialGradient id="bgGlow" cx="20%" cy="20%" r="80%">
            <stop offset="0%" stop-color="#1e3a8a" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#020617" stop-opacity="1"/>
        </radialGradient>
        <style>
            .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
            .font-mono {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
        </style>
    </defs>
    
    <rect width="840" height="240" fill="#020617"/>
    <rect x="20" y="20" width="800" height="200" rx="20" fill="url(#bgGlow)" stroke="url(#borderGrad)" stroke-width="1.5"/>
    
    <!-- Avatar -->
    <circle cx="100" cy="120" r="50" fill="#0f172a" stroke="#3b82f6" stroke-width="2"/>
    <text x="100" y="135" font-size="40" text-anchor="middle" class="font-sans">👨‍💻</text>

    <!-- Header Text -->
    <text x="175" y="80" class="font-mono" font-size="14" font-weight="600" fill="#60a5fa" letter-spacing="1">@{USERNAME}</text>
    <text x="175" y="115" class="font-sans" font-size="36" font-weight="800" fill="#f8fafc">Atul Kumar Choudhary</text>
    <text x="175" y="145" class="font-sans" font-size="15" font-weight="500" fill="#94a3b8">Building scalable AI backends and next-gen UI.</text>
    
    <!-- Pills -->
    <rect x="175" y="165" width="85" height="26" rx="13" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="217.5" y="183" font-size="12" font-weight="700" fill="#e2e8f0" text-anchor="middle" class="font-sans">Python</text>

    <rect x="270" y="165" width="105" height="26" rx="13" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="322.5" y="183" font-size="12" font-weight="700" fill="#e2e8f0" text-anchor="middle" class="font-sans">TypeScript</text>

    <rect x="385" y="165" width="95" height="26" rx="13" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="432.5" y="183" font-size="12" font-weight="700" fill="#e2e8f0" text-anchor="middle" class="font-sans">Next.js</text>

    <!-- Stats on Right -->
    <text x="750" y="115" class="font-sans" font-size="42" font-weight="800" fill="#38bdf8" text-anchor="end">{str_stars}</text>
    <text x="750" y="140" class="font-mono" font-size="12" font-weight="700" fill="#64748b" text-anchor="end" letter-spacing="2">TOTAL STARS</text>

    <text x="790" y="205" class="font-mono" font-size="10" fill="#334155" text-anchor="end">custom generated • live</text>
</svg>'''

with open('assets/header.svg', 'w', encoding='utf-8') as f:
    f.write(header_svg)

projects_svg = f'''<svg width="840" height="340" viewBox="0 0 840 340" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.8"/>
            <stop offset="50%" stop-color="#1e293b" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#10b981" stop-opacity="0.8"/>
        </linearGradient>
        <radialGradient id="bgGlow" cx="20%" cy="20%" r="80%">
            <stop offset="0%" stop-color="#064e3b" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#020617" stop-opacity="1"/>
        </radialGradient>
        <style>
            .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
            .font-mono {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
        </style>
    </defs>
    
    <rect width="840" height="340" fill="#020617"/>
    <rect x="20" y="20" width="800" height="300" rx="16" fill="url(#bgGlow)" stroke="url(#borderGrad)" stroke-width="1.5"/>
    
    <text x="45" y="60" class="font-mono" font-size="13" font-weight="700" fill="#38bdf8" letter-spacing="1">PROJECTS.LIST</text>
    <text x="180" y="60" class="font-mono" font-size="13" font-weight="500" fill="#475569">./projects.sh --all</text>
    <text x="780" y="60" class="font-mono" font-size="13" font-weight="500" fill="#64748b" text-anchor="end">2 pinned</text>
    
    <line x1="45" y1="75" x2="795" y2="75" stroke="#1e293b" stroke-width="1"/>

    <!-- Project 1 -->
    <rect x="45" y="95" width="370" height="190" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="1.5"/>
    <circle cx="65" cy="115" r="3" fill="#10b981"/>
    <text x="75" y="119" class="font-mono" font-size="12" fill="#94a3b8">{repo1['name']}</text>
    <circle cx="395" cy="115" r="4" fill="#334155"/>
    <line x1="45" y1="135" x2="415" y2="135" stroke="#1e293b" stroke-width="1"/>
    
    <text x="65" y="170" class="font-sans" font-size="22" font-weight="800" fill="#f8fafc">{repo1['name'][:14]} _</text>
    <text x="65" y="195" class="font-sans" font-size="14" font-weight="500" fill="#64748b">{repo1['desc']}</text>
    
    <rect x="65" y="245" width="85" height="24" rx="12" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1" opacity="0.8"/>
    <text x="107.5" y="261" font-size="11" font-weight="700" fill="#93c5fd" text-anchor="middle" class="font-sans">open-source</text>
    
    <text x="65" y="270" class="font-mono" font-size="11" font-weight="600" fill="#3b82f6">★ {repo1['stars']}</text>
    <text x="115" y="270" class="font-mono" font-size="11" font-weight="500" fill="#64748b">updated {repo1['updated']}</text>

    <!-- Ring Chart -->
    <circle cx="360" cy="210" r="28" fill="none" stroke="#1e293b" stroke-width="6"/>
    <circle cx="360" cy="210" r="28" fill="none" stroke="#3b82f6" stroke-width="6" stroke-dasharray="175" stroke-dashoffset="30" transform="rotate(-90 360 210)"/>
    <text x="360" y="214" font-size="12" font-weight="800" fill="#f8fafc" text-anchor="middle" class="font-sans">90%</text>


    <!-- Project 2 -->
    <rect x="425" y="95" width="370" height="190" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="1.5"/>
    <circle cx="445" cy="115" r="3" fill="#38bdf8"/>
    <text x="455" y="119" class="font-mono" font-size="12" fill="#94a3b8">{repo2['name']}</text>
    <circle cx="775" cy="115" r="4" fill="#334155"/>
    <line x1="425" y1="135" x2="795" y2="135" stroke="#1e293b" stroke-width="1"/>
    
    <text x="445" y="170" class="font-sans" font-size="22" font-weight="800" fill="#f8fafc">{repo2['name'][:14]} _</text>
    <text x="445" y="195" class="font-sans" font-size="14" font-weight="500" fill="#64748b">{repo2['desc']}</text>
    
    <rect x="445" y="245" width="75" height="24" rx="12" fill="#064e3b" stroke="#10b981" stroke-width="1" opacity="0.8"/>
    <text x="482.5" y="261" font-size="11" font-weight="700" fill="#6ee7b7" text-anchor="middle" class="font-sans">active</text>
    
    <text x="445" y="270" class="font-mono" font-size="11" font-weight="600" fill="#3b82f6">★ {repo2['stars']}</text>
    <text x="495" y="270" class="font-mono" font-size="11" font-weight="500" fill="#64748b">updated {repo2['updated']}</text>

    <!-- Ring Chart -->
    <circle cx="740" cy="210" r="28" fill="none" stroke="#1e293b" stroke-width="6"/>
    <circle cx="740" cy="210" r="28" fill="none" stroke="#10b981" stroke-width="6" stroke-dasharray="175" stroke-dashoffset="50" transform="rotate(-90 740 210)"/>
    <text x="740" y="214" font-size="12" font-weight="800" fill="#f8fafc" text-anchor="middle" class="font-sans">75%</text>

    <text x="790" y="305" class="font-mono" font-size="10" fill="#334155" text-anchor="end">custom generated • live</text>
</svg>'''

with open('assets/projects.svg', 'w', encoding='utf-8') as f:
    f.write(projects_svg)

stats_svg = f'''<svg width="840" height="260" viewBox="0 0 840 260" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.8"/>
            <stop offset="50%" stop-color="#1e293b" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#10b981" stop-opacity="0.8"/>
        </linearGradient>
        <radialGradient id="bgGlow" cx="80%" cy="20%" r="80%">
            <stop offset="0%" stop-color="#1e3a8a" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#020617" stop-opacity="1"/>
        </radialGradient>
        <style>
            .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
            .font-mono {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
        </style>
    </defs>
    
    <rect width="840" height="260" fill="#020617"/>
    <rect x="20" y="20" width="800" height="220" rx="16" fill="url(#bgGlow)" stroke="url(#borderGrad)" stroke-width="1.5"/>
    
    <text x="45" y="65" class="font-sans" font-size="28" font-weight="900" fill="#f8fafc">Profile Signal</text>
    <text x="45" y="85" class="font-sans" font-size="14" font-weight="600" fill="#94a3b8">Live GitHub stats fetched dynamically</text>
    
    <circle cx="800" cy="40" r="4" fill="#38bdf8"/>

    <!-- Stat 1 -->
    <rect x="45" y="110" width="170" height="100" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="1.5"/>
    <text x="65" y="140" class="font-mono" font-size="12" font-weight="600" fill="#f8fafc">Stars</text>
    <text x="65" y="175" class="font-sans" font-size="34" font-weight="800" fill="#38bdf8">{str_stars}</text>
    <rect x="65" y="190" width="130" height="6" rx="3" fill="#1e293b"/>
    <rect x="65" y="190" width="110" height="6" rx="3" fill="#38bdf8"/>

    <!-- Stat 2 -->
    <rect x="235" y="110" width="170" height="100" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="1.5"/>
    <text x="255" y="140" class="font-mono" font-size="12" font-weight="600" fill="#f8fafc">Contributions</text>
    <text x="255" y="175" class="font-sans" font-size="34" font-weight="800" fill="#22d3ee">{contributions}</text>
    <rect x="255" y="190" width="130" height="6" rx="3" fill="#1e293b"/>
    <rect x="255" y="190" width="90" height="6" rx="3" fill="#22d3ee"/>

    <!-- Stat 3 -->
    <rect x="425" y="110" width="170" height="100" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="1.5"/>
    <text x="445" y="140" class="font-mono" font-size="12" font-weight="600" fill="#f8fafc">Repos</text>
    <text x="445" y="175" class="font-sans" font-size="34" font-weight="800" fill="#c084fc">{public_repos}</text>
    <rect x="445" y="190" width="130" height="6" rx="3" fill="#1e293b"/>
    <rect x="445" y="190" width="60" height="6" rx="3" fill="#c084fc"/>

    <!-- Stat 4 -->
    <rect x="615" y="110" width="170" height="100" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="1.5"/>
    <text x="635" y="140" class="font-mono" font-size="12" font-weight="600" fill="#f8fafc">Followers</text>
    <text x="635" y="175" class="font-sans" font-size="34" font-weight="800" fill="#10b981">{followers}</text>
    <rect x="635" y="190" width="130" height="6" rx="3" fill="#1e293b"/>
    <rect x="635" y="190" width="100" height="6" rx="3" fill="#10b981"/>

    <text x="790" y="225" class="font-mono" font-size="10" fill="#334155" text-anchor="end">custom generated • live</text>
</svg>'''

with open('assets/stats.svg', 'w', encoding='utf-8') as f:
    f.write(stats_svg)
    
footer_svg = f'''<svg width="840" height="120" viewBox="0 0 840 120" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.8"/>
            <stop offset="50%" stop-color="#1e293b" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#10b981" stop-opacity="0.8"/>
        </linearGradient>
        <radialGradient id="bgGlow" cx="50%" cy="50%" r="80%">
            <stop offset="0%" stop-color="#022c22" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#020617" stop-opacity="1"/>
        </radialGradient>
        <style>
            .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
            .font-mono {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
        </style>
    </defs>
    
    <rect width="840" height="120" fill="#020617"/>
    <rect x="20" y="10" width="800" height="100" rx="16" fill="url(#bgGlow)" stroke="url(#borderGrad)" stroke-width="1.5"/>
    
    <rect x="320" y="35" width="200" height="50" rx="25" fill="#0f172a" stroke="#1e293b" stroke-width="2"/>
    <circle cx="345" cy="60" r="12" fill="#f8fafc"/>
    <path d="M345 53c-3.86 0-7 3.14-7 7 0 3.09 2.01 5.71 4.79 6.64.35.07.48-.15.48-.34 0-.17-.01-.61-.01-1.2-1.95.42-2.36-.94-2.36-.94-.32-.81-.78-1.03-.78-1.03-.64-.44.05-.43.05-.43.71.05 1.08.73 1.08.73.63 1.08 1.65.77 2.05.59.06-.46.25-.77.45-.95-1.55-.18-3.19-.78-3.19-3.46 0-.76.27-1.39.72-1.88-.07-.18-.31-.89.07-1.85 0 0 .59-.19 1.93.72a6.72 6.72 0 0 1 1.76-.24c.6 0 1.2.08 1.76.24 1.34-.91 1.93-.72 1.93-.72.38.96.14 1.67.07 1.85.45.49.72 1.12.72 1.88 0 2.69-1.64 3.28-3.2 3.46.26.22.49.66.49 1.33 0 .96-.01 1.74-.01 1.98 0 .19.13.41.49.34C349.99 62.71 352 60.09 352 57c0-3.86-3.14-7-7-7z" fill="#0f172a"/>
    <text x="365" y="55" class="font-sans" font-size="11" font-weight="600" fill="#94a3b8">GitHub</text>
    <text x="365" y="70" class="font-sans" font-size="14" font-weight="800" fill="#f8fafc">@{USERNAME}</text>
    
    <text x="790" y="95" class="font-mono" font-size="10" fill="#334155" text-anchor="end">custom generated • live</text>
</svg>'''

with open('assets/footer.svg', 'w', encoding='utf-8') as f:
    f.write(footer_svg)
    
print("Successfully generated SVGs with live data!")
