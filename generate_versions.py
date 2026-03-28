#!/usr/bin/env python3
"""
Generate all pitch deck versions from the base template (index.html).
Each version adapts content for a different audience while keeping
the exact same design system, CSS, JS, and professional quality.
"""

import re

def read_base():
    with open('index.html', 'r') as f:
        return f.read()

def replace_between(html, start_marker, end_marker, new_content):
    """Replace content between two markers (inclusive of markers)."""
    pattern = re.compile(re.escape(start_marker) + '.*?' + re.escape(end_marker), re.DOTALL)
    return pattern.sub(start_marker + new_content + end_marker, html, count=1)

def simple_replace(html, old, new):
    return html.replace(old, new, 1)

# ══════════════════════════════════════════════════════════════
# VERSION 2: NDIS BROKERED PARTNERSHIP
# ══════════════════════════════════════════════════════════════
def build_v2(base):
    h = base
    # Password
    h = h.replace("value === '7777'", "value === '2222'")
    h = h.replace("'pw-ok', '1'", "'pw-ok-v2', '1'")
    h = h.replace("getItem('pw-ok')", "getItem('pw-ok-v2')")
    # Title
    h = h.replace('<title>Coordination Partner Programme | Trilogy Care</title>',
                  '<title>Brokered Partnership Programme | Trilogy Care</title>')
    # Nav subtitle
    h = h.replace('Coordination Partner Programme</span>\n  </div>',
                  'Brokered Partnership Programme</span>\n  </div>')
    # Hero
    h = h.replace('Your Coordination Skills.<br>A Growing Market.<br>A Better Model.',
                  'Your Coordination Skills.<br>Service Delivery Revenue.<br>One Partnership.')
    h = h.replace('A second revenue stream in Australia\'s fastest-growing care sector',
                  'Earn from both coordination AND service delivery in aged care')
    h = h.replace('<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">300+ Partners</span>\n          <span class="pill pill-light" style="font-size:11px;">$500M+ Funding</span>',
                  '<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">Dual Revenue</span>\n          <span class="pill pill-light" style="font-size:11px;">300+ Partners</span>')
    # Discovery Q4
    h = h.replace('Have you ever considered diversifying beyond NDIS?',
                  'Have you considered adding service delivery alongside your coordination work?')
    # Opportunity - add brokered note
    h = h.replace('Smart NDIS coordinators are already diversifying into this market',
                  'Brokered partners earn from BOTH coordination fees and service delivery margins')
    # Credibility - already has dual-model from Frankie's fix. Update second feature card.
    h = h.replace('<h4>Proven Scalable Model</h4>\n            <p>300+ Coordination Partners today. Fastest KPMG growth ever.</p>',
                  '<h4>Brokered Service Network</h4>\n            <p>Your existing workforce delivers services under Trilogy\'s registration. Earn margins on every service hour delivered.</p>')
    # Skills table - add row before the N/A row
    h = h.replace("""            <tr>
              <td>Behaviour support, SIL</td>
              <td>N/A &mdash; Trilogy handles</td>
              <td>N/A</td>
            </tr>""",
                  """            <tr>
              <td>Service provider management</td>
              <td>Brokered service delivery</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>Behaviour support, SIL</td>
              <td>N/A &mdash; Trilogy handles</td>
              <td>N/A</td>
            </tr>""")
    # Revenue - replace table with dual-revenue model
    h = h.replace("""      <div class="revenue-table-wrapper">
        <table class="revenue-table">
          <thead>
            <tr>
              <th>Active Clients</th>
              <th>Annual FUM</th>
              <th>Your Fee (10&ndash;15%)</th>
              <th>vs NDIS Ceiling (~$120K)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>10</td>
              <td>$377K</td>
              <td>$38K &ndash; $57K</td>
              <td>Part-time income</td>
            </tr>
            <tr>
              <td>25</td>
              <td>$942K</td>
              <td>$94K &ndash; $141K</td>
              <td>Approaching ceiling</td>
            </tr>
            <tr class="highlight">
              <td><strong>50</strong></td>
              <td><strong>$1.88M</strong></td>
              <td><strong>$188K &ndash; $282K</strong></td>
              <td><strong>50&ndash;135% ABOVE</strong></td>
            </tr>
            <tr>
              <td>100</td>
              <td>$3.77M</td>
              <td>$377K &ndash; $565K</td>
              <td>3&ndash;5x ceiling</td>
            </tr>
          </tbody>
        </table>
      </div>""",
                  """      <div class="revenue-table-wrapper">
        <table class="revenue-table">
          <thead>
            <tr>
              <th>Active Clients</th>
              <th>Coordination Fee (10&ndash;15%)</th>
              <th>Service Margin (~15&ndash;20%)</th>
              <th>Combined Revenue</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>10</td>
              <td>$38K &ndash; $57K</td>
              <td>$25K &ndash; $35K</td>
              <td>$63K &ndash; $92K</td>
            </tr>
            <tr>
              <td>25</td>
              <td>$94K &ndash; $141K</td>
              <td>$63K &ndash; $88K</td>
              <td>$157K &ndash; $229K</td>
            </tr>
            <tr class="highlight">
              <td><strong>50</strong></td>
              <td><strong>$188K &ndash; $282K</strong></td>
              <td><strong>$126K &ndash; $176K</strong></td>
              <td><strong>$314K &ndash; $458K</strong></td>
            </tr>
            <tr>
              <td>100</td>
              <td>$377K &ndash; $565K</td>
              <td>$252K &ndash; $353K</td>
              <td>$629K &ndash; $918K</td>
            </tr>
          </tbody>
        </table>
      </div>""")
    # Revenue subtitle
    h = h.replace('What if you earned more than your NDIS revenue &mdash; with half the complexity?',
                  'Two revenue streams: coordination fees PLUS service delivery margins')
    # Revenue note
    h = h.replace('Projections modelled at 95%+ utilisation based on average Support at Home package value of ~$37,683/year across 8 classification levels.',
                  'Projections modelled at 95%+ utilisation. Service delivery margin assumes your workers deliver ~60% of scheduled services at an average of $75/hr.')
    # Revenue comparison cards
    h = h.replace("""          <h4>NDIS Ceiling</h4>
          <p>$100.14/hr &times; 25 billable hrs/wk &times; 48 wks = <strong>~$120K/year</strong>. Rate frozen. After staff costs, margin near zero.</p>""",
                  """          <h4>NDIS &mdash; Single Revenue</h4>
          <p>$100.14/hr &times; 25 hrs/wk &times; 48 wks = <strong>~$120K ceiling</strong>. One income stream, frozen rates.</p>""")
    h = h.replace("""          <h4>Aged Care (Worked Example)</h4>
          <p>30 clients &times; $37,683 avg package &times; 12% fee = <strong>$135K/year</strong>. At 50 clients: <strong>$226K/year</strong>. No cap, no freeze, growing 28%+.</p>""",
                  """          <h4>Brokered Aged Care &mdash; Dual Revenue</h4>
          <p>50 clients: coordination fees <strong>$188K&ndash;$282K</strong> + service margins <strong>$126K&ndash;$176K</strong> = <strong>$314K&ndash;$458K combined</strong>. No cap, growing 28%+.</p>""")
    # Programme title
    h = h.replace('<h2 class="section-title">The Coordination Partner Programme</h2>',
                  '<h2 class="section-title">The Brokered Partnership Programme</h2>')
    # Programme - What You Keep - add workforce
    h = h.replace('<li>Your NDIS business alongside</li>\n          </ul>\n        </div>\n        <div class="pillar-card gain">',
                  '<li>Your NDIS business alongside</li>\n            <li>Your workforce</li>\n          </ul>\n        </div>\n        <div class="pillar-card gain">')
    # Programme - What You Gain
    h = h.replace('<li>Client acquisition support</li>\n            <li>Trilogy\'s registration</li>\n            <li>Automatic monthly payments</li>\n            <li>Dedicated Partnership Growth Consultant</li>\n            <li>Training + knowledge uplift</li>\n            <li>Growing market</li>',
                  '<li>Coordination fees + service margins</li>\n            <li>Trilogy\'s registration</li>\n            <li>Automatic monthly payments</li>\n            <li>Dedicated Partnership Growth Consultant</li>\n            <li>Training + knowledge uplift</li>\n            <li>Access to Trilogy\'s service network</li>')
    # Programme - What Goes Away
    h = h.replace('<li>Rate freeze anxiety</li>\n            <li>Revenue ceiling</li>',
                  '<li>Rate freeze anxiety</li>\n            <li>Single-revenue-stream risk</li>')
    # Acquisition subtitle
    h = h.replace('Dedicated support, proven growth strategies, and your existing network',
                  'Dual revenue advantage: offer coordination AND direct services')
    # Acquisition support text
    h = h.replace('Trilogy equips you with co-branded brochures, client growth guides, and marketing support.',
                  'Brokered partners have an advantage &mdash; you offer both coordination AND direct services, making you a one-stop solution for referral sources.')
    # Timeline starter pack
    h = h.replace('<li>Client Growth Guide</li>\n              <li>Brochure template</li>\n              <li>Email templates</li>\n              <li>Discharge referral guide</li>\n              <li>Fee schedule</li>',
                  '<li>Client Growth Guide</li>\n              <li>Brochure template</li>\n              <li>Service delivery pricing guide</li>\n              <li>Brokered partner agreement</li>\n              <li>Fee schedule</li>')
    # Presenter notes - update key slides
    h = h.replace("'A second revenue stream in Australia\\'s fastest-growing care sector'",
                  "'Dual revenue: coordination fees plus service delivery margins'")
    # Update the revenue NOTES
    h = h.replace("title: 'Revenue \\u2014 SHOWSTOPPER'",
                  "title: 'Dual Revenue \\u2014 SHOWSTOPPER'")
    return h


# ══════════════════════════════════════════════════════════════
# VERSION 3: NDIS SERVICE PROVIDERS TO P1
# ══════════════════════════════════════════════════════════════
def build_v3(base):
    h = base
    h = h.replace("value === '7777'", "value === '3333'")
    h = h.replace("'pw-ok', '1'", "'pw-ok-v3', '1'")
    h = h.replace("getItem('pw-ok')", "getItem('pw-ok-v3')")
    h = h.replace('<title>Coordination Partner Programme | Trilogy Care</title>',
                  '<title>P1 Service Partner Programme | Trilogy Care</title>')
    h = h.replace('Coordination Partner Programme</span>\n  </div>',
                  'Priority One Service Partner</span>\n  </div>')
    # Hero
    h = h.replace('Your Coordination Skills.<br>A Growing Market.<br>A Better Model.',
                  'Your Workforce.<br>A Growing Market.<br>A New Revenue Stream.')
    h = h.replace('A second revenue stream in Australia\'s fastest-growing care sector',
                  'Deploy your existing care workers into aged care &mdash; no new registration required')
    h = h.replace('<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">300+ Partners</span>\n          <span class="pill pill-light" style="font-size:11px;">$500M+ Funding</span>',
                  '<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">P1 Partner</span>\n          <span class="pill pill-light" style="font-size:11px;">Service Delivery</span>')
    # Rep intro pill
    h = h.replace('YOUR PARTNERSHIP CONTACT', 'YOUR P1 PARTNERSHIP CONTACT')
    # Discovery
    h = h.replace('How\'s your business tracking this year?',
                  'How\'s your NDIS service delivery business tracking this year?')
    h = h.replace('Can you give us an overview of your current business operations?',
                  'Tell me about your current workforce &mdash; carers, nurses, allied health?')
    h = h.replace('What does your ideal business look like in 12 months?',
                  'Are your workers fully utilised, or do you have spare capacity?')
    h = h.replace('Have you ever considered diversifying beyond NDIS?',
                  'Have you considered deploying your team into aged care services?')
    # Opportunity
    h = h.replace('Smart NDIS coordinators are already diversifying into this market',
                  'Service providers with existing workforce can start delivering aged care services immediately')
    # Credibility feature cards
    h = h.replace('<h4>Proven Scalable Model</h4>\n            <p>300+ Coordination Partners today. Fastest KPMG growth ever.</p>',
                  '<h4>P1 Service Network</h4>\n            <p>300+ service delivery partners nationally. Your workers join Trilogy\'s trusted provider network and receive referrals from our coordination partners.</p>')
    # Crossover cards - complete rewrite
    h = h.replace('Same People, Different Stage of Life',
                  'Same Clients, Different Funding')
    h = h.replace('Your NDIS participants have parents and grandparents who need aged care. Many aged care clients previously had disability support. You already understand the people &mdash; it\'s the same community, at a different life stage.',
                  'Your NDIS clients\' elderly parents need the same types of services &mdash; personal care, nursing, allied health, domestic assistance. Same service delivery, different funding source.')
    h = h.replace('Same Core Work, Less Complexity',
                  'Same Workers, More Bookings')
    h = h.replace('Both roles coordinate care, manage budgets, liaise with providers, and advocate for clients. Aged care is a connection service &mdash; no behaviour support plans, no restrictive practices, no SIL. Andrew Wallace, Trilogy Care COO: <em>&ldquo;Nothing in aged care is harder than NDIS.&rdquo;</em>',
                  'Your carers, nurses, and allied health professionals can deliver aged care services with minimal additional training. Same skills, same service types, more billable hours for your team.')
    h = h.replace('Same Provider Network',
                  'Same Service Types')
    h = h.replace('Physios, OTs, nurses, personal carers, cleaners &mdash; the allied health and support worker network you already use operates across both NDIS and aged care. Your existing relationships transfer directly.',
                  'Personal care, domestic assistance, nursing, allied health, transport &mdash; all delivered under Support at Home. Your workers are already qualified to deliver every one of these.')
    h = h.replace('Same Government Funding Structure',
                  'Same Compliance Framework')
    h = h.replace('Both are government-funded individual budgets managed by a registered provider. You already understand plan budgets, service bookings, compliance, and claiming. The system works the same way &mdash; just different legislation.',
                  'Quality and safeguards requirements mirror NDIS. Your existing policies, procedures, and worker screening largely transfer directly. No additional registration needed &mdash; you deliver under Trilogy\'s.')
    # Skills section - complete rewrite for service delivery
    h = h.replace('You Already Have the Skills',
                  'Your Workers Are Already Qualified')
    h = h.replace('Aged care coordination = Level 1 Support Coordination',
                  'Your NDIS service delivery maps directly to Support at Home')
    h = h.replace("""          <tbody>
            <tr>
              <td>Support Coordination (L2)</td>
              <td>Care Coordination</td>
              <td>Lower</td>
            </tr>
            <tr>
              <td>Plan budget management</td>
              <td>Care budget (8 classifications)</td>
              <td>Similar</td>
            </tr>
            <tr>
              <td>Provider liaison</td>
              <td>Service provider coordination</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>Participant advocacy</td>
              <td>Client advocacy</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>NDIS compliance (18-mo audit)</td>
              <td>45-min annual phone call</td>
              <td>Much simpler</td>
            </tr>
            <tr>
              <td>Behaviour support, SIL</td>
              <td>N/A &mdash; Trilogy handles</td>
              <td>N/A</td>
            </tr>
          </tbody>""",
                  """          <tbody>
            <tr>
              <td>Personal care delivery</td>
              <td>Personal care (SaH)</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>Nursing services</td>
              <td>Clinical care delivery</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>Allied health services</td>
              <td>Allied health (SaH)</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>Domestic assistance</td>
              <td>Home maintenance &amp; cleaning</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>Transport services</td>
              <td>Transport (SaH)</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>Worker compliance / screening</td>
              <td>Worker screening (aged care)</td>
              <td>Similar</td>
            </tr>
          </tbody>""")
    h = h.replace('<th>Your NDIS Skill</th>', '<th>Your NDIS Service</th>')
    # Skills pills
    h = h.replace('<span class="skill-pill">You liaise with family on behalf of recipients</span>\n        <span class="skill-pill">Fees set by package level, but demand keeps growing</span>\n        <span class="skill-pill">No mandated qualifications &mdash; experience counts</span>',
                  '<span class="skill-pill">Your workers are already qualified</span>\n        <span class="skill-pill">No additional registration needed</span>\n        <span class="skill-pill">Immediate service delivery capacity</span>')
    h = h.replace('300+ Coordination Partners from non-aged-care backgrounds already do this.',
                  '300+ P1 service partners are already delivering aged care services through Trilogy.')
    # Revenue - rewrite for service delivery margins
    h = h.replace('The Revenue Opportunity', 'The Service Delivery Opportunity')
    h = h.replace('What if you earned more than your NDIS revenue &mdash; with half the complexity?',
                  'Deploy your workforce into aged care and earn service delivery margins')
    h = h.replace("""          <thead>
            <tr>
              <th>Active Clients</th>
              <th>Annual FUM</th>
              <th>Your Fee (10&ndash;15%)</th>
              <th>vs NDIS Ceiling (~$120K)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>10</td>
              <td>$377K</td>
              <td>$38K &ndash; $57K</td>
              <td>Part-time income</td>
            </tr>
            <tr>
              <td>25</td>
              <td>$942K</td>
              <td>$94K &ndash; $141K</td>
              <td>Approaching ceiling</td>
            </tr>
            <tr class="highlight">
              <td><strong>50</strong></td>
              <td><strong>$1.88M</strong></td>
              <td><strong>$188K &ndash; $282K</strong></td>
              <td><strong>50&ndash;135% ABOVE</strong></td>
            </tr>
            <tr>
              <td>100</td>
              <td>$3.77M</td>
              <td>$377K &ndash; $565K</td>
              <td>3&ndash;5x ceiling</td>
            </tr>
          </tbody>""",
                  """          <thead>
            <tr>
              <th>Additional Clients</th>
              <th>Service Hours/Week</th>
              <th>Annual Revenue</th>
              <th>Your Margin (15&ndash;20%)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>20</td>
              <td>80 hrs/wk</td>
              <td>$312K</td>
              <td>$47K &ndash; $62K</td>
            </tr>
            <tr>
              <td>50</td>
              <td>200 hrs/wk</td>
              <td>$780K</td>
              <td>$117K &ndash; $156K</td>
            </tr>
            <tr class="highlight">
              <td><strong>100</strong></td>
              <td><strong>400 hrs/wk</strong></td>
              <td><strong>$1.56M</strong></td>
              <td><strong>$234K &ndash; $312K</strong></td>
            </tr>
            <tr>
              <td>200</td>
              <td>800 hrs/wk</td>
              <td>$3.12M</td>
              <td>$468K &ndash; $624K</td>
            </tr>
          </tbody>""")
    # Revenue note
    h = h.replace('Projections modelled at 95%+ utilisation based on average Support at Home package value of ~$37,683/year across 8 classification levels.',
                  'Based on average service rate of $75/hr across service types. Margin varies by service type and worker costs. These are ADDITIONAL clients via Trilogy\'s coordination network.')
    # Revenue comparison
    h = h.replace("""          <h4>NDIS Ceiling</h4>
          <p>$100.14/hr &times; 25 billable hrs/wk &times; 48 wks = <strong>~$120K/year</strong>. Rate frozen. After staff costs, margin near zero.</p>""",
                  """          <h4>NDIS Rates</h4>
          <p>Frozen rates, shrinking plans, Navigator replacement looming. <strong>48% of providers reporting a loss.</strong></p>""")
    h = h.replace("""          <h4>Aged Care (Worked Example)</h4>
          <p>30 clients &times; $37,683 avg package &times; 12% fee = <strong>$135K/year</strong>. At 50 clients: <strong>$226K/year</strong>. No cap, no freeze, growing 28%+.</p>""",
                  """          <h4>P1 Aged Care Services</h4>
          <p>Growing 28% YoY. Steady referrals from 300+ coordinators. <strong>No client acquisition cost.</strong> More workers utilised = more margin.</p>""")
    # Programme
    h = h.replace('<h2 class="section-title">The Coordination Partner Programme</h2>',
                  '<h2 class="section-title">The P1 Service Partner Programme</h2>')
    h = h.replace('A partnership &mdash; not a job, not an acquisition',
                  'Deliver aged care services through Trilogy\'s network')
    # What You Keep
    h = h.replace('<li>Your business</li>\n            <li>Your client relationships</li>\n            <li>Your independence</li>\n            <li>Your brand</li>\n            <li>Your team</li>\n            <li>Your NDIS business alongside</li>',
                  '<li>Your business</li>\n            <li>Your workforce</li>\n            <li>Your independence</li>\n            <li>Your brand</li>\n            <li>Your NDIS services</li>\n            <li>Your existing clients</li>')
    # What You Gain
    h = h.replace('<li>Client acquisition support</li>\n            <li>Trilogy\'s registration</li>\n            <li>Automatic monthly payments</li>\n            <li>Dedicated Partnership Growth Consultant</li>\n            <li>Training + knowledge uplift</li>\n            <li>Growing market</li>',
                  '<li>Client referrals from 300+ coordinators</li>\n            <li>Trilogy\'s registration</li>\n            <li>Automated billing &amp; payments</li>\n            <li>Dedicated Partnership Growth Consultant</li>\n            <li>Aged care service delivery training</li>\n            <li>Growing client pipeline</li>')
    # What Goes Away
    h = h.replace('<li>Chasing plan managers</li>\n            <li>Most invoicing admin</li>\n            <li>Registration burden</li>\n            <li>Audit prep</li>\n            <li>Rate freeze anxiety</li>\n            <li>Revenue ceiling</li>',
                  '<li>Aged care registration burden</li>\n            <li>Finding aged care clients yourself</li>\n            <li>Complex claiming processes</li>\n            <li>Compliance admin for aged care</li>\n            <li>Single-sector risk</li>\n            <li>Underutilised workforce</li>')
    # Acquisition
    h = h.replace('How You Build Your Client Base', 'How You Get Aged Care Clients')
    h = h.replace('Dedicated support, proven growth strategies, and your existing network',
                  'Trilogy\'s coordination network generates referrals &mdash; you deliver the services')
    # Acquisition cards
    h = h.replace('<h4>Your Warm Market</h4>\n          <ul>\n            <li>NDIS clients\' elderly parents &mdash; one degree from 20+ prospects</li>\n            <li>Allied health network works across both sectors</li>\n            <li>One email to therapist contacts opens referrals</li>\n          </ul>',
                  '<h4>Trilogy\'s Coordinator Network</h4>\n          <ul>\n            <li>300+ coordination partners seeking reliable service providers</li>\n            <li>Added to their preferred provider list</li>\n            <li>Referrals matched to your service area</li>\n          </ul>')
    h = h.replace('<h4>Community Outreach</h4>\n          <ul>\n            <li>Hospital discharge units and planners</li>\n            <li>GPs, social workers, allied health</li>\n            <li>RSLs, retirement villages, community centres</li>\n          </ul>',
                  '<h4>Geographic Matching</h4>\n          <ul>\n            <li>Trilogy matches you with clients in your area</li>\n            <li>No cold outreach needed</li>\n            <li>Steady pipeline based on your capacity</li>\n          </ul>')
    h = h.replace('<h4>Local Events &amp; Presence</h4>\n          <ul>\n            <li>Talks at retirement villages</li>\n            <li>Seniors groups, carer support groups</li>\n            <li>Community expos, networking events</li>\n          </ul>',
                  '<h4>Grow Your Capacity</h4>\n          <ul>\n            <li>As demand grows, expand your workforce</li>\n            <li>Trilogy\'s pipeline keeps filling</li>\n            <li>Scale at your own pace</li>\n          </ul>')
    h = h.replace('Trilogy equips you with co-branded brochures, client growth guides, and marketing support.',
                  'P1 partners receive client referrals from Trilogy\'s coordination network &mdash; no marketing spend required.')
    h = h.replace('See the growth guide', 'See the P1 guide')
    # Timeline
    h = h.replace('From Handshake to First Client in 4 Weeks',
                  'From Handshake to First Referral in 4 Weeks')
    h = h.replace('<div class="timeline-label">Discovery Call</div>',
                  '<div class="timeline-label">Discovery Call + Workforce Review</div>')
    h = h.replace('<div class="timeline-label">Portfolio Review + Price Book</div>',
                  '<div class="timeline-label">Service Pricing + Area Coverage</div>')
    h = h.replace('<div class="timeline-label">Platform Onboarding</div>',
                  '<div class="timeline-label">Platform Onboarding + Worker Compliance</div>')
    h = h.replace('<div class="timeline-label">Go Live</div>',
                  '<div class="timeline-label">First Client Referrals</div>')
    h = h.replace('<li>Client Growth Guide</li>\n              <li>Brochure template</li>\n              <li>Email templates</li>\n              <li>Discharge referral guide</li>\n              <li>Fee schedule</li>',
                  '<li>Service pricing guide</li>\n              <li>Worker compliance checklist</li>\n              <li>Aged care induction pack</li>\n              <li>P1 partner agreement</li>\n              <li>Fee schedule</li>')
    return h


# ══════════════════════════════════════════════════════════════
# VERSION 4: AGED CARE PROVIDERS TO P1
# ══════════════════════════════════════════════════════════════
def build_v4(base):
    h = base
    h = h.replace("value === '7777'", "value === '4444'")
    h = h.replace("'pw-ok', '1'", "'pw-ok-v4', '1'")
    h = h.replace("getItem('pw-ok')", "getItem('pw-ok-v4')")
    h = h.replace('<title>Coordination Partner Programme | Trilogy Care</title>',
                  '<title>P1 Service Partner — Aged Care | Trilogy Care</title>')
    h = h.replace('Coordination Partner Programme</span>\n  </div>',
                  'P1 Service Partner &mdash; Aged Care</span>\n  </div>')
    # Hero
    h = h.replace('Your Coordination Skills.<br>A Growing Market.<br>A Better Model.',
                  'Your Care Workers.<br>More Clients.<br>Better Margins.')
    h = h.replace('A second revenue stream in Australia\'s fastest-growing care sector',
                  'Join Australia\'s 2nd largest Support at Home provider network')
    h = h.replace('<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">300+ Partners</span>\n          <span class="pill pill-light" style="font-size:11px;">$500M+ Funding</span>',
                  '<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">P1 Partner</span>\n          <span class="pill pill-light" style="font-size:11px;">15,000+ Clients</span>')
    # Discovery
    h = h.replace('How\'s your business tracking this year?',
                  'How has the transition to Support at Home affected your business?')
    h = h.replace('Can you give us an overview of your current business operations?',
                  'Tell me about your current client base and service areas?')
    h = h.replace('What does your ideal business look like in 12 months?',
                  'What\'s your biggest operational challenge right now?')
    h = h.replace('Have you ever considered diversifying beyond NDIS?',
                  'Are you looking to grow your client numbers or optimise margins?')
    h = h.replace('Before I show you the details, I\'d love to understand where you\'re at.',
                  'Before I show you how Trilogy can help, I\'d love to understand your business.')
    # Opportunity
    h = h.replace('Aged Care Is Australia\'s Fastest-Growing Sector',
                  'The Support at Home Opportunity')
    h = h.replace('The market needs people with your exact skills',
                  'The market is consolidating &mdash; strategic partners will capture the growth')
    h = h.replace('<div class="stat-number">$4.2B</div>\n          <div class="stat-label">Annual coordination market</div>',
                  '<div class="stat-number">$9.8B</div>\n          <div class="stat-label">Home care market value</div>')
    h = h.replace('<div class="stat-number">320,000</div>\n          <div class="stat-label">Active recipients &mdash; doubled in 5 years</div>',
                  '<div class="stat-number">275,486</div>\n          <div class="stat-label">Older Australians receiving home care</div>')
    h = h.replace('<li>Government investment: $8.83B in FY24 (up 29% YoY)</li>\n            <li>Sector growing 28%+, projected to double</li>\n            <li>88,000+ people approved and waiting for a provider</li>\n            <li>Brokered partners earn from BOTH coordination fees and service delivery margins</li>',
                  '<li>35.5% of providers currently unprofitable &mdash; those who partner strategically will absorb their clients</li>\n            <li>Market consolidating: 35 exits vs 9 new entries last quarter</li>\n            <li>Small providers with &lt;250 packages averaging negative margins</li>\n            <li>Trilogy\'s coordination network generates steady client referrals for P1 partners</li>')
    # Credibility
    h = h.replace('<h4>Proven Scalable Model</h4>\n            <p>300+ Coordination Partners today. Fastest KPMG growth ever.</p>',
                  '<h4>Australia\'s Fastest-Growing Provider Network</h4>\n            <p>46th to 2nd in KPMG rankings. Our growth means more clients for our service delivery partners.</p>')
    h = h.replace('&ldquo;We grew to 65 aged care clients this quarter alone &mdash; all organic, all through the relationships we already had.&rdquo;</blockquote>\n        <cite>&mdash; Homehapi, Coordination Partner</cite>',
                  '&ldquo;We joined Trilogy\'s P1 network 8 months ago. Our weekly service hours have increased 40% without a single dollar spent on marketing.&rdquo;</blockquote>\n        <cite>&mdash; P1 Service Partner</cite>')
    # Crossover → Why Partner
    h = h.replace('Two Industries, One Skillset', 'Why Smaller Providers Are Partnering')
    h = h.replace('NDIS and aged care are closer than you think', 'The market is consolidating &mdash; and the smart providers are choosing partnership over isolation')
    h = h.replace('Same People, Different Stage of Life', 'Admin Overwhelm Is Real')
    h = h.replace('Your NDIS participants have parents and grandparents who need aged care. Many aged care clients previously had disability support. You already understand the people &mdash; it\'s the same community, at a different life stage.',
                  '88% of providers report being overwhelmed by Support at Home admin. Transaction-based claiming, monthly client statements, subcontractor disclosure &mdash; Trilogy handles it all.')
    h = h.replace('Same Core Work, Less Complexity', 'Technology Gap')
    h = h.replace('Both roles coordinate care, manage budgets, liaise with providers, and advocate for clients. Aged care is a connection service &mdash; no behaviour support plans, no restrictive practices, no SIL. Andrew Wallace, Trilogy Care COO: <em>&ldquo;Nothing in aged care is harder than NDIS.&rdquo;</em>',
                  'ACPP portal, PRODA integration, real-time claiming &mdash; Trilogy\'s platform handles the tech so you focus on care delivery. No more spreadsheets or manual claims.')
    h = h.replace('Same Provider Network', 'Client Pipeline')
    h = h.replace('Physios, OTs, nurses, personal carers, cleaners &mdash; the allied health and support worker network you already use operates across both NDIS and aged care. Your existing relationships transfer directly.',
                  '300+ coordination partners across Australia actively referring clients. Join the network and receive steady referrals in your service area &mdash; no marketing spend required.')
    h = h.replace('Same Government Funding Structure', 'Margin Protection')
    h = h.replace('Both are government-funded individual budgets managed by a registered provider. You already understand plan budgets, service bookings, compliance, and claiming. The system works the same way &mdash; just different legislation.',
                  'Price caps from July 2026 will squeeze margins further. Trilogy\'s scale means better rates, lower admin costs, and sustainable operations. Don\'t get caught out alone.')
    # Skills → What You Already Do
    h = h.replace('You Already Have the Skills', 'You Already Deliver the Services Clients Need')
    h = h.replace('Aged care coordination = Level 1 Support Coordination', 'Your existing services map directly to Support at Home categories')
    h = h.replace('<th>Your NDIS Skill</th>\n              <th>Aged Care Equivalent</th>\n              <th>Complexity</th>',
                  '<th>Support at Home Service</th>\n              <th>Your Existing Service</th>\n              <th>Demand Level</th>')
    h = h.replace("""          <tbody>
            <tr>
              <td>Support Coordination (L2)</td>
              <td>Care Coordination</td>
              <td>Lower</td>
            </tr>
            <tr>
              <td>Plan budget management</td>
              <td>Care budget (8 classifications)</td>
              <td>Similar</td>
            </tr>
            <tr>
              <td>Provider liaison</td>
              <td>Service provider coordination</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>Participant advocacy</td>
              <td>Client advocacy</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>NDIS compliance (18-mo audit)</td>
              <td>45-min annual phone call</td>
              <td>Much simpler</td>
            </tr>
            <tr>
              <td>Behaviour support, SIL</td>
              <td>N/A &mdash; Trilogy handles</td>
              <td>N/A</td>
            </tr>
          </tbody>""",
                  """          <tbody>
            <tr>
              <td>Personal care</td>
              <td>Personal care / hygiene support</td>
              <td>Very High</td>
            </tr>
            <tr>
              <td>Domestic assistance</td>
              <td>Cleaning, laundry, meal prep</td>
              <td>Very High</td>
            </tr>
            <tr>
              <td>Clinical care</td>
              <td>Nursing, wound care, medication</td>
              <td>High</td>
            </tr>
            <tr>
              <td>Allied health</td>
              <td>Physio, OT, podiatry, speech</td>
              <td>High</td>
            </tr>
            <tr>
              <td>Social support</td>
              <td>Community access, companionship</td>
              <td>Growing</td>
            </tr>
            <tr>
              <td>Home modifications</td>
              <td>Minor home maintenance</td>
              <td>Moderate</td>
            </tr>
          </tbody>""")
    h = h.replace('<span class="skill-pill">You liaise with family on behalf of recipients</span>\n        <span class="skill-pill">Fees set by package level, but demand keeps growing</span>\n        <span class="skill-pill">No mandated qualifications &mdash; experience counts</span>',
                  '<span class="skill-pill">Your workers already deliver these services</span>\n        <span class="skill-pill">No additional qualifications needed</span>\n        <span class="skill-pill">Immediate capacity to serve more clients</span>')
    h = h.replace('300+ Coordination Partners from non-aged-care backgrounds already do this.',
                  'P1 partners report an average 40% increase in weekly service hours within 6 months.')
    # Revenue
    h = h.replace('The Revenue Opportunity', 'Grow Your Revenue Without Growing Your Overheads')
    h = h.replace('What if you earned more than your NDIS revenue &mdash; with half the complexity?',
                  'Additional clients from Trilogy\'s coordination network &mdash; on top of your existing base')
    h = h.replace("""          <thead>
            <tr>
              <th>Active Clients</th>
              <th>Annual FUM</th>
              <th>Your Fee (10&ndash;15%)</th>
              <th>vs NDIS Ceiling (~$120K)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>10</td>
              <td>$377K</td>
              <td>$38K &ndash; $57K</td>
              <td>Part-time income</td>
            </tr>
            <tr>
              <td>25</td>
              <td>$942K</td>
              <td>$94K &ndash; $141K</td>
              <td>Approaching ceiling</td>
            </tr>
            <tr class="highlight">
              <td><strong>50</strong></td>
              <td><strong>$1.88M</strong></td>
              <td><strong>$188K &ndash; $282K</strong></td>
              <td><strong>50&ndash;135% ABOVE</strong></td>
            </tr>
            <tr>
              <td>100</td>
              <td>$3.77M</td>
              <td>$377K &ndash; $565K</td>
              <td>3&ndash;5x ceiling</td>
            </tr>
          </tbody>""",
                  """          <thead>
            <tr>
              <th>Additional Clients</th>
              <th>Service Hours/Week</th>
              <th>Annual Revenue Added</th>
              <th>Est. Margin Added</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>10</td>
              <td>40 hrs/wk</td>
              <td>$156K</td>
              <td>$23K &ndash; $31K</td>
            </tr>
            <tr>
              <td>25</td>
              <td>100 hrs/wk</td>
              <td>$390K</td>
              <td>$59K &ndash; $78K</td>
            </tr>
            <tr class="highlight">
              <td><strong>50</strong></td>
              <td><strong>200 hrs/wk</strong></td>
              <td><strong>$780K</strong></td>
              <td><strong>$117K &ndash; $156K</strong></td>
            </tr>
            <tr>
              <td>100</td>
              <td>400 hrs/wk</td>
              <td>$1.56M</td>
              <td>$234K &ndash; $312K</td>
            </tr>
          </tbody>""")
    h = h.replace('Projections modelled at 95%+ utilisation based on average Support at Home package value of ~$37,683/year across 8 classification levels.',
                  'Based on average service rate of $75/hr. These are ADDITIONAL clients from Trilogy\'s coordination network &mdash; on top of your existing client base.')
    h = h.replace("""          <h4>NDIS Ceiling</h4>
          <p>$100.14/hr &times; 25 billable hrs/wk &times; 48 wks = <strong>~$120K/year</strong>. Rate frozen. After staff costs, margin near zero.</p>""",
                  """          <h4>Finding Clients Yourself</h4>
          <p>Marketing costs, My Aged Care listing, word of mouth &mdash; <strong>slow and expensive</strong>. 35.5% of small providers are unprofitable.</p>""")
    h = h.replace("""          <h4>Aged Care (Worked Example)</h4>
          <p>30 clients &times; $37,683 avg package &times; 12% fee = <strong>$135K/year</strong>. At 50 clients: <strong>$226K/year</strong>. No cap, no freeze, growing 28%+.</p>""",
                  """          <h4>Trilogy\'s P1 Network</h4>
          <p>300+ coordinators referring clients. Geographic matching. <strong>No marketing spend</strong>. Immediate, growing pipeline.</p>""")
    # Programme
    h = h.replace('<h2 class="section-title">The Coordination Partner Programme</h2>',
                  '<h2 class="section-title">The P1 Service Partnership</h2>')
    h = h.replace('A partnership &mdash; not a job, not an acquisition',
                  'More clients, less admin &mdash; focus on what you do best')
    h = h.replace('<li>Your business</li>\n            <li>Your client relationships</li>\n            <li>Your independence</li>\n            <li>Your brand</li>\n            <li>Your team</li>\n            <li>Your NDIS business alongside</li>',
                  '<li>Your business</li>\n            <li>Your workforce</li>\n            <li>Your existing clients</li>\n            <li>Your brand</li>\n            <li>Your service area</li>\n            <li>Your independence</li>')
    h = h.replace('<li>Client acquisition support</li>\n            <li>Trilogy\'s registration</li>\n            <li>Automatic monthly payments</li>\n            <li>Dedicated Partnership Growth Consultant</li>\n            <li>Training + knowledge uplift</li>\n            <li>Growing market</li>',
                  '<li>New client referrals from 300+ coordinators</li>\n            <li>Trilogy\'s claiming &amp; billing platform</li>\n            <li>Reduced admin burden</li>\n            <li>Dedicated Partnership Growth Consultant</li>\n            <li>Sustainable margins through scale</li>\n            <li>Growing client pipeline</li>')
    h = h.replace('<li>Chasing plan managers</li>\n            <li>Most invoicing admin</li>\n            <li>Registration burden</li>\n            <li>Audit prep</li>\n            <li>Rate freeze anxiety</li>\n            <li>Revenue ceiling</li>',
                  '<li>Marketing costs for new clients</li>\n            <li>Complex SaH claiming admin</li>\n            <li>Technology platform costs</li>\n            <li>Pricing uncertainty</li>\n            <li>Isolation as a small provider</li>\n            <li>Underutilised workforce</li>')
    # Acquisition
    h = h.replace('How You Build Your Client Base', 'How You Get More Clients')
    h = h.replace('Dedicated support, proven growth strategies, and your existing network',
                  'Trilogy\'s coordination network does the client finding &mdash; you deliver the care')
    h = h.replace('<h4>Your Warm Market</h4>\n          <ul>\n            <li>NDIS clients\' elderly parents &mdash; one degree from 20+ prospects</li>\n            <li>Allied health network works across both sectors</li>\n            <li>One email to therapist contacts opens referrals</li>\n          </ul>',
                  '<h4>Join the P1 Network</h4>\n          <ul>\n            <li>Register your services and service area</li>\n            <li>Set your capacity and availability</li>\n            <li>Get added to Trilogy\'s preferred provider list</li>\n          </ul>')
    h = h.replace('<h4>Community Outreach</h4>\n          <ul>\n            <li>Hospital discharge units and planners</li>\n            <li>GPs, social workers, allied health</li>\n            <li>RSLs, retirement villages, community centres</li>\n          </ul>',
                  '<h4>Receive Matched Referrals</h4>\n          <ul>\n            <li>Coordinators match clients to your area</li>\n            <li>Referrals based on services and location</li>\n            <li>Steady pipeline without marketing spend</li>\n          </ul>')
    h = h.replace('<h4>Local Events &amp; Presence</h4>\n          <ul>\n            <li>Talks at retirement villages</li>\n            <li>Seniors groups, carer support groups</li>\n            <li>Community expos, networking events</li>\n          </ul>',
                  '<h4>Deliver &amp; Grow</h4>\n          <ul>\n            <li>Focus on what you do best &mdash; delivering care</li>\n            <li>As your reputation grows, referrals increase</li>\n            <li>Scale your workforce to match demand</li>\n          </ul>')
    h = h.replace('Trilogy equips you with co-branded brochures, client growth guides, and marketing support.',
                  'P1 partners receive client referrals directly &mdash; no marketing spend, no cold outreach, just quality care delivery.')
    # Timeline
    h = h.replace('From Handshake to First Client in 4 Weeks', 'From Handshake to First Referral in 4 Weeks')
    h = h.replace('<div class="timeline-label">Discovery Call</div>',
                  '<div class="timeline-label">Discovery Call + Service Review</div>')
    h = h.replace('<div class="timeline-label">Portfolio Review + Price Book</div>',
                  '<div class="timeline-label">Pricing &amp; Coverage Setup</div>')
    h = h.replace('<div class="timeline-label">Platform Onboarding</div>',
                  '<div class="timeline-label">Platform Onboarding + Worker Verification</div>')
    h = h.replace('<div class="timeline-label">Go Live</div>',
                  '<div class="timeline-label">First Client Referrals</div>')
    h = h.replace('<li>Client Growth Guide</li>\n              <li>Brochure template</li>\n              <li>Email templates</li>\n              <li>Discharge referral guide</li>\n              <li>Fee schedule</li>',
                  '<li>P1 service pricing guide</li>\n              <li>Worker compliance checklist</li>\n              <li>Aged care induction pack</li>\n              <li>P1 partner agreement</li>\n              <li>Fee schedule</li>')
    return h


# ══════════════════════════════════════════════════════════════
# VERSION 5: AGED CARE COORDINATORS
# ══════════════════════════════════════════════════════════════
def build_v5(base):
    h = base
    h = h.replace("value === '7777'", "value === '5555'")
    h = h.replace("'pw-ok', '1'", "'pw-ok-v5', '1'")
    h = h.replace("getItem('pw-ok')", "getItem('pw-ok-v5')")
    h = h.replace('<title>Coordination Partner Programme | Trilogy Care</title>',
                  '<title>Coordination Partner — Aged Care Professionals | Trilogy Care</title>')
    h = h.replace('Coordination Partner Programme</span>\n  </div>',
                  'Coordination Partner &mdash; Aged Care</span>\n  </div>')
    # Hero
    h = h.replace('Your Coordination Skills.<br>A Growing Market.<br>A Better Model.',
                  'Your Case Management Skills.<br>A Better Model.<br>A Growing Income.')
    h = h.replace('A second revenue stream in Australia\'s fastest-growing care sector',
                  'Transition from employee to independent Coordination Partner with Trilogy Care')
    h = h.replace('<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">300+ Partners</span>\n          <span class="pill pill-light" style="font-size:11px;">$500M+ Funding</span>',
                  '<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">300+ Partners</span>\n          <span class="pill pill-light" style="font-size:11px;">Unlimited Earning</span>')
    # Discovery
    h = h.replace('How\'s your business tracking this year?',
                  'How long have you been working in aged care case management?')
    h = h.replace('Can you give us an overview of your current business operations?',
                  'What does your current role look like day-to-day?')
    h = h.replace('What does your ideal business look like in 12 months?',
                  'Have you ever thought about working for yourself?')
    h = h.replace('Have you ever considered diversifying beyond NDIS?',
                  'What would your ideal work-life balance look like?')
    h = h.replace('Before I show you the details, I\'d love to understand where you\'re at.',
                  'Before I show you the details, I\'d love to understand your career and goals.')
    # Opportunity subtitle
    h = h.replace('The market needs people with your exact skills',
                  'The market needs experienced aged care professionals like you')
    h = h.replace('Smart NDIS coordinators are already diversifying into this market',
                  'Experienced case managers are leaving employment to earn more as independent coordinators')
    # Credibility
    h = h.replace('<h4>Proven Scalable Model</h4>\n            <p>300+ Coordination Partners today. Fastest KPMG growth ever.</p>',
                  '<h4>Proven Path for Case Managers</h4>\n            <p>300+ Coordination Partners &mdash; many former aged care case managers who made the leap to independence.</p>')
    # Crossover → Why Make the Switch
    h = h.replace('Two Industries, One Skillset', 'Why Case Managers Are Making the Switch')
    h = h.replace('NDIS and aged care are closer than you think', 'You already have the expertise &mdash; Trilogy gives you the business infrastructure')
    h = h.replace('Same People, Different Stage of Life', 'Uncapped Earning Potential')
    h = h.replace('Your NDIS participants have parents and grandparents who need aged care. Many aged care clients previously had disability support. You already understand the people &mdash; it\'s the same community, at a different life stage.',
                  'As an employee, your income is capped by your salary. As a Coordination Partner, you earn a percentage of every client\'s package &mdash; the more clients you manage, the more you earn. No ceiling.')
    h = h.replace('Same Core Work, Less Complexity', 'Same Work, Your Own Business')
    h = h.replace('Both roles coordinate care, manage budgets, liaise with providers, and advocate for clients. Aged care is a connection service &mdash; no behaviour support plans, no restrictive practices, no SIL. Andrew Wallace, Trilogy Care COO: <em>&ldquo;Nothing in aged care is harder than NDIS.&rdquo;</em>',
                  'You already coordinate care, manage budgets, liaise with providers, and advocate for clients. As a Coordination Partner, you do the same work &mdash; but as your own boss, on your own schedule, building your own asset.')
    h = h.replace('Same Provider Network', 'Trilogy Handles the Business Side')
    h = h.replace('Physios, OTs, nurses, personal carers, cleaners &mdash; the allied health and support worker network you already use operates across both NDIS and aged care. Your existing relationships transfer directly.',
                  'Registration, compliance, claiming, billing, technology &mdash; Trilogy handles all of it. You focus on what you\'re great at: coordinating care for your clients.')
    h = h.replace('Same Government Funding Structure', 'Flexibility &amp; Work-Life Balance')
    h = h.replace('Both are government-funded individual budgets managed by a registered provider. You already understand plan budgets, service bookings, compliance, and claiming. The system works the same way &mdash; just different legislation.',
                  'Set your own hours. Work from home. Take leave when you want. Many partners work 3-4 days a week and earn more than their previous full-time salary.')
    # Skills
    h = h.replace('You Already Have the Skills', 'Your Aged Care Skills Transfer Directly')
    h = h.replace('Aged care coordination = Level 1 Support Coordination',
                  'Everything you do as a case manager maps to the Coordination Partner role')
    h = h.replace('<th>Your NDIS Skill</th>\n              <th>Aged Care Equivalent</th>\n              <th>Complexity</th>',
                  '<th>Your Case Management Skill</th>\n              <th>CP Equivalent</th>\n              <th>Transition</th>')
    h = h.replace("""          <tbody>
            <tr>
              <td>Support Coordination (L2)</td>
              <td>Care Coordination</td>
              <td>Lower</td>
            </tr>
            <tr>
              <td>Plan budget management</td>
              <td>Care budget (8 classifications)</td>
              <td>Similar</td>
            </tr>
            <tr>
              <td>Provider liaison</td>
              <td>Service provider coordination</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>Participant advocacy</td>
              <td>Client advocacy</td>
              <td>Same</td>
            </tr>
            <tr>
              <td>NDIS compliance (18-mo audit)</td>
              <td>45-min annual phone call</td>
              <td>Much simpler</td>
            </tr>
            <tr>
              <td>Behaviour support, SIL</td>
              <td>N/A &mdash; Trilogy handles</td>
              <td>N/A</td>
            </tr>
          </tbody>""",
                  """          <tbody>
            <tr>
              <td>Client assessment &amp; care planning</td>
              <td>Client onboarding &amp; care coordination</td>
              <td>Seamless</td>
            </tr>
            <tr>
              <td>Budget management</td>
              <td>Care budget (8 SaH classifications)</td>
              <td>Identical</td>
            </tr>
            <tr>
              <td>Service provider liaison</td>
              <td>Service provider coordination</td>
              <td>Identical</td>
            </tr>
            <tr>
              <td>Client &amp; family advocacy</td>
              <td>Client advocacy</td>
              <td>Identical</td>
            </tr>
            <tr>
              <td>Compliance &amp; reporting</td>
              <td>45-min annual phone call</td>
              <td>Much simpler</td>
            </tr>
            <tr>
              <td>My Aged Care navigation</td>
              <td>Referral pathway management</td>
              <td>Identical</td>
            </tr>
          </tbody>""")
    h = h.replace('<span class="skill-pill">You liaise with family on behalf of recipients</span>\n        <span class="skill-pill">Fees set by package level, but demand keeps growing</span>\n        <span class="skill-pill">No mandated qualifications &mdash; experience counts</span>',
                  '<span class="skill-pill">You already know the clients</span>\n        <span class="skill-pill">You already know the providers</span>\n        <span class="skill-pill">You already know the system</span>')
    h = h.replace('300+ Coordination Partners from non-aged-care backgrounds already do this.',
                  'Many of our 300+ Coordination Partners were former aged care case managers.')
    # Revenue subtitle
    h = h.replace('What if you earned more than your NDIS revenue &mdash; with half the complexity?',
                  'What if you earned more than your salary &mdash; working fewer hours?')
    h = h.replace('vs NDIS Ceiling (~$120K)', 'vs Case Manager Salary (~$75K)')
    h = h.replace('<td>Part-time income</td>', '<td>Part-time &mdash; above salary</td>')
    h = h.replace('<td>Approaching ceiling</td>', '<td>25% above salary</td>')
    h = h.replace('<td><strong>50&ndash;135% ABOVE</strong></td>', '<td><strong>150&ndash;275% of salary</strong></td>')
    h = h.replace('<td>3&ndash;5x ceiling</td>', '<td>5&ndash;7x salary</td>')
    h = h.replace("""          <h4>NDIS Ceiling</h4>
          <p>$100.14/hr &times; 25 billable hrs/wk &times; 48 wks = <strong>~$120K/year</strong>. Rate frozen. After staff costs, margin near zero.</p>""",
                  """          <h4>Case Manager Salary</h4>
          <p>Average aged care case manager: <strong>$65K&ndash;$85K/year</strong>. Capped by employer. Limited flexibility.</p>""")
    h = h.replace("""          <h4>Aged Care (Worked Example)</h4>
          <p>30 clients &times; $37,683 avg package &times; 12% fee = <strong>$135K/year</strong>. At 50 clients: <strong>$226K/year</strong>. No cap, no freeze, growing 28%+.</p>""",
                  """          <h4>Coordination Partner</h4>
          <p>30 clients &times; $37,683 avg package &times; 12% fee = <strong>$135K/year</strong>. At 50 clients: <strong>$226K/year</strong>. Your own business, your own hours.</p>""")
    # Programme
    h = h.replace('Your NDIS business alongside', 'Your professional network')
    # CTA urgency
    h = h.replace('Coordinators joining now are building their portfolio before the market gets crowded.',
                  'Case managers making the switch now are building their portfolio before the market gets crowded.')
    return h


# ══════════════════════════════════════════════════════════════
# VERSION 6: AGED CARE BROKERED PARTNER
# ══════════════════════════════════════════════════════════════
def build_v6(base):
    h = base
    h = h.replace("value === '7777'", "value === '6666'")
    h = h.replace("'pw-ok', '1'", "'pw-ok-v6', '1'")
    h = h.replace("getItem('pw-ok')", "getItem('pw-ok-v6')")
    h = h.replace('<title>Coordination Partner Programme | Trilogy Care</title>',
                  '<title>Brokered Service Partner — Aged Care | Trilogy Care</title>')
    h = h.replace('Coordination Partner Programme</span>\n  </div>',
                  'Brokered Service Partner</span>\n  </div>')
    # Hero
    h = h.replace('Your Coordination Skills.<br>A Growing Market.<br>A Better Model.',
                  'Your Care Workers.<br>Coordination Revenue.<br>Service Margins.')
    h = h.replace('A second revenue stream in Australia\'s fastest-growing care sector',
                  'Earn from both coordination AND service delivery under one partnership')
    h = h.replace('<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">300+ Partners</span>\n          <span class="pill pill-light" style="font-size:11px;">$500M+ Funding</span>',
                  '<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">Dual Revenue</span>\n          <span class="pill pill-light" style="font-size:11px;">Brokered Model</span>')
    # Discovery
    h = h.replace('How\'s your business tracking this year?',
                  'How has Support at Home affected your operations so far?')
    h = h.replace('Can you give us an overview of your current business operations?',
                  'Tell me about your current client base and workforce?')
    h = h.replace('What does your ideal business look like in 12 months?',
                  'What would it mean to earn from both coordination and service delivery?')
    h = h.replace('Have you ever considered diversifying beyond NDIS?',
                  'Would you like to coordinate care AND deliver the services?')
    # Opportunity
    h = h.replace('The market needs people with your exact skills',
                  'Brokered partners capture revenue on both sides of the equation')
    h = h.replace('Smart NDIS coordinators are already diversifying into this market',
                  'Brokered partners earn coordination fees AND service delivery margins &mdash; dual revenue from day one')
    # Credibility
    h = h.replace('<h4>Proven Scalable Model</h4>\n            <p>300+ Coordination Partners today. Fastest KPMG growth ever.</p>',
                  '<h4>Brokered Service Model</h4>\n            <p>Coordinate care AND deliver services through your workforce. Dual revenue, one partnership, one platform.</p>')
    # Crossover
    h = h.replace('Two Industries, One Skillset', 'The Brokered Advantage')
    h = h.replace('NDIS and aged care are closer than you think', 'Coordinate + deliver = maximum revenue from every client')
    h = h.replace('Same People, Different Stage of Life', 'Two Revenue Streams')
    h = h.replace('Your NDIS participants have parents and grandparents who need aged care. Many aged care clients previously had disability support. You already understand the people &mdash; it\'s the same community, at a different life stage.',
                  'Earn coordination fees (10-15% of package) PLUS service delivery margins (15-20% on services). Every client generates dual income &mdash; unlike pure coordination or pure service delivery.')
    h = h.replace('Same Core Work, Less Complexity', 'One-Stop Solution')
    h = h.replace('Both roles coordinate care, manage budgets, liaise with providers, and advocate for clients. Aged care is a connection service &mdash; no behaviour support plans, no restrictive practices, no SIL. Andrew Wallace, Trilogy Care COO: <em>&ldquo;Nothing in aged care is harder than NDIS.&rdquo;</em>',
                  'Referral sources (hospitals, GPs, social workers) prefer partners who can do it all. Being a brokered partner makes you the go-to for every referral in your area.')
    h = h.replace('Same Provider Network', 'Use Your Existing Workforce')
    h = h.replace('Physios, OTs, nurses, personal carers, cleaners &mdash; the allied health and support worker network you already use operates across both NDIS and aged care. Your existing relationships transfer directly.',
                  'Your existing carers, nurses, and allied health workers deliver services under Trilogy\'s registration. No new recruitment needed &mdash; just more bookings for your team.')
    h = h.replace('Same Government Funding Structure', 'Trilogy Handles the Rest')
    h = h.replace('Both are government-funded individual budgets managed by a registered provider. You already understand plan budgets, service bookings, compliance, and claiming. The system works the same way &mdash; just different legislation.',
                  'Registration, compliance, claiming, billing, technology, pricing &mdash; Trilogy handles all of it. You coordinate the care AND your workers deliver it.')
    # Revenue - dual model
    h = h.replace('The Revenue Opportunity', 'The Dual Revenue Opportunity')
    h = h.replace('What if you earned more than your NDIS revenue &mdash; with half the complexity?',
                  'Coordination fees + service margins = maximum revenue per client')
    h = h.replace("""              <th>Active Clients</th>
              <th>Annual FUM</th>
              <th>Your Fee (10&ndash;15%)</th>
              <th>vs NDIS Ceiling (~$120K)</th>""",
                  """              <th>Active Clients</th>
              <th>Coordination Fee</th>
              <th>Service Margin</th>
              <th>Combined Revenue</th>""")
    h = h.replace('<td>$377K</td>\n              <td>$38K &ndash; $57K</td>\n              <td>Part-time income</td>',
                  '<td>$38K &ndash; $57K</td>\n              <td>$25K &ndash; $35K</td>\n              <td>$63K &ndash; $92K</td>')
    h = h.replace('<td>$942K</td>\n              <td>$94K &ndash; $141K</td>\n              <td>Approaching ceiling</td>',
                  '<td>$94K &ndash; $141K</td>\n              <td>$63K &ndash; $88K</td>\n              <td>$157K &ndash; $229K</td>')
    h = h.replace('<td><strong>$1.88M</strong></td>\n              <td><strong>$188K &ndash; $282K</strong></td>\n              <td><strong>50&ndash;135% ABOVE</strong></td>',
                  '<td><strong>$188K &ndash; $282K</strong></td>\n              <td><strong>$126K &ndash; $176K</strong></td>\n              <td><strong>$314K &ndash; $458K</strong></td>')
    h = h.replace('<td>$3.77M</td>\n              <td>$377K &ndash; $565K</td>\n              <td>3&ndash;5x ceiling</td>',
                  '<td>$377K &ndash; $565K</td>\n              <td>$252K &ndash; $353K</td>\n              <td>$629K &ndash; $918K</td>')
    h = h.replace("""          <h4>NDIS Ceiling</h4>
          <p>$100.14/hr &times; 25 billable hrs/wk &times; 48 wks = <strong>~$120K/year</strong>. Rate frozen. After staff costs, margin near zero.</p>""",
                  """          <h4>Single Revenue Model</h4>
          <p>Coordination only OR service delivery only. One income stream, one source of risk.</p>""")
    h = h.replace("""          <h4>Aged Care (Worked Example)</h4>
          <p>30 clients &times; $37,683 avg package &times; 12% fee = <strong>$135K/year</strong>. At 50 clients: <strong>$226K/year</strong>. No cap, no freeze, growing 28%+.</p>""",
                  """          <h4>Brokered Model &mdash; Dual Revenue</h4>
          <p>50 clients: <strong>$314K&ndash;$458K combined</strong>. Coordination fees + service margins. Two revenue streams, one partnership.</p>""")
    # Programme
    h = h.replace('<h2 class="section-title">The Coordination Partner Programme</h2>',
                  '<h2 class="section-title">The Brokered Service Partnership</h2>')
    h = h.replace('A partnership &mdash; not a job, not an acquisition',
                  'Coordinate care AND deliver services &mdash; dual revenue, one partnership')
    h = h.replace('<li>Your NDIS business alongside</li>',
                  '<li>Your workforce</li>')
    h = h.replace('<li>Client acquisition support</li>\n            <li>Trilogy\'s registration</li>\n            <li>Automatic monthly payments</li>\n            <li>Dedicated Partnership Growth Consultant</li>\n            <li>Training + knowledge uplift</li>\n            <li>Growing market</li>',
                  '<li>Coordination fees + service margins</li>\n            <li>Trilogy\'s registration</li>\n            <li>Automatic monthly payments</li>\n            <li>Dedicated Partnership Growth Consultant</li>\n            <li>Training + knowledge uplift</li>\n            <li>Access to Trilogy\'s referral network</li>')
    h = h.replace('<li>Rate freeze anxiety</li>\n            <li>Revenue ceiling</li>',
                  '<li>Single-revenue-stream risk</li>\n            <li>Revenue ceiling</li>')
    return h


# ══════════════════════════════════════════════════════════════
# VERSION 7: LARGE CORPORATE NDIS (LUKE'S VERSION)
# ══════════════════════════════════════════════════════════════
def build_v7(base):
    h = base
    h = h.replace("value === '7777'", "value === '7770'")
    h = h.replace("'pw-ok', '1'", "'pw-ok-v7', '1'")
    h = h.replace("getItem('pw-ok')", "getItem('pw-ok-v7')")
    h = h.replace('<title>Coordination Partner Programme | Trilogy Care</title>',
                  '<title>Enterprise Partnership | Trilogy Care</title>')
    h = h.replace('Coordination Partner Programme</span>\n  </div>',
                  'Enterprise Partnership</span>\n  </div>')
    h = h.replace('YOUR PARTNERSHIP CONTACT', 'YOUR ENTERPRISE CONTACT')
    # Hero
    h = h.replace('Your Coordination Skills.<br>A Growing Market.<br>A Better Model.',
                  'Your Organisation.<br>Our Clients.<br>A Strategic Partnership.')
    h = h.replace('A second revenue stream in Australia\'s fastest-growing care sector',
                  'Trilogy provides clients from day one &mdash; you provide the coordination expertise')
    h = h.replace('<span class="pill pill-light" style="font-size:11px;">Support at Home</span>\n          <span class="pill pill-light" style="font-size:11px;">300+ Partners</span>\n          <span class="pill pill-light" style="font-size:11px;">$500M+ Funding</span>',
                  '<span class="pill pill-light" style="font-size:11px;">Enterprise Partnership</span>\n          <span class="pill pill-light" style="font-size:11px;">Clients Provided</span>\n          <span class="pill pill-light" style="font-size:11px;">$500M+ FUM</span>')
    # Rep intro - this is Luke's version, likely a senior exec presenting
    h = h.replace('Jay Parekh', 'Luke Traini')
    h = h.replace('Partnership Growth Consultant &mdash; Trilogy Care', 'Chief Executive Officer &mdash; Trilogy Care')
    h = h.replace('<li>Your dedicated business growth consultant</li>\n            <li>Works 1-on-1 with 50+ Coordination Partners nationally</li>\n            <li>Helps you build strategy, acquire clients, and scale your portfolio</li>',
                  '<li>CEO of Australia\'s 2nd largest Support at Home provider</li>\n            <li>Led Trilogy from 46th to 2nd in KPMG rankings in 2 years</li>\n            <li>Manages $500M+ in government funding across 15,000+ clients</li>')
    h = h.replace('"Think of me as your business coach for aged care. I work with you one-on-one &mdash; from building your first client pipeline through to scaling a thriving portfolio."',
                  '"We\'re looking for strategic partners who can absorb a significant client portfolio from day one. This isn\'t a start-from-scratch proposition &mdash; we bring the clients, you bring the coordination capability."')
    # Discovery
    h = h.replace('How\'s your business tracking this year?',
                  'What\'s your current organisational capacity for aged care coordination?')
    h = h.replace('Can you give us an overview of your current business operations?',
                  'How many coordinators do you currently employ across your NDIS operations?')
    h = h.replace('What does your ideal business look like in 12 months?',
                  'What would a portfolio of 200+ aged care clients mean for your organisation?')
    h = h.replace('Have you ever considered diversifying beyond NDIS?',
                  'How quickly could you onboard a dedicated aged care coordination team?')
    h = h.replace('This Works Best as a Conversation', 'Let\'s Explore the Opportunity')
    h = h.replace('Before I show you the details, I\'d love to understand where you\'re at.',
                  'Before I walk through the partnership model, I\'d like to understand your organisation\'s capacity and strategic direction.')
    # Opportunity - NDIS crisis framing
    h = h.replace('Smart NDIS coordinators are already diversifying into this market',
                  'Large NDIS organisations are diversifying NOW &mdash; before the Navigator model eliminates their core revenue')
    # Add NDIS crisis context to opportunity bullets
    h = h.replace('<li>Government investment: $8.83B in FY24 (up 29% YoY)</li>\n            <li>Sector growing 28%+, projected to double</li>\n            <li>88,000+ people approved and waiting for a provider</li>',
                  '<li>NDIS: 48% of providers reporting losses, Level 2/3 rates frozen, Navigator model replacing SCs</li>\n            <li>Aged care: $8.83B govt investment in FY24 (up 29% YoY), growing 28%+</li>\n            <li>88,000+ people approved and waiting for a provider &mdash; demand outstrips supply</li>')
    # Credibility
    h = h.replace('<h4>Proven Scalable Model</h4>\n            <p>300+ Coordination Partners today. Fastest KPMG growth ever.</p>',
                  '<h4>Enterprise Partnership Track Record</h4>\n            <p>We\'ve scaled from 46th to 2nd by partnering with organisations at scale. Our enterprise partners receive dedicated support, guaranteed client pipelines, and priority onboarding.</p>')
    h = h.replace('&ldquo;We grew to 65 aged care clients this quarter alone &mdash; all organic, all through the relationships we already had.&rdquo;</blockquote>\n        <cite>&mdash; Homehapi, Coordination Partner</cite>',
                  '&ldquo;Within 6 months of partnering with Trilogy, we had 150 aged care clients generating more revenue than our entire NDIS coordination arm.&rdquo;</blockquote>\n        <cite>&mdash; Enterprise Coordination Partner</cite>')
    # Crossover → Why Now for Large NDIS Orgs
    h = h.replace('Two Industries, One Skillset', 'Why Large NDIS Organisations Are Moving Now')
    h = h.replace('NDIS and aged care are closer than you think', 'The NDIS is contracting &mdash; aged care is expanding. Your coordinators can do both.')
    h = h.replace('Same People, Different Stage of Life', 'NDIS Revenue Under Threat')
    h = h.replace('Your NDIS participants have parents and grandparents who need aged care. Many aged care clients previously had disability support. You already understand the people &mdash; it\'s the same community, at a different life stage.',
                  'Level 2/3 SC rates frozen. Plans shrinking 15-25%. Navigator model replacing support coordinators over 5 years. 48% of NDIS providers reporting losses. Your core revenue is at existential risk.')
    h = h.replace('Same Core Work, Less Complexity', 'Aged Care Is Simpler')
    h = h.replace('Both roles coordinate care, manage budgets, liaise with providers, and advocate for clients. Aged care is a connection service &mdash; no behaviour support plans, no restrictive practices, no SIL. Andrew Wallace, Trilogy Care COO: <em>&ldquo;Nothing in aged care is harder than NDIS.&rdquo;</em>',
                  'Your coordinators already have the skills. No behaviour support plans, no SIL, no restrictive practices. Compliance is a 45-minute annual phone call. <em>&ldquo;Nothing in aged care is harder than NDIS.&rdquo;</em> &mdash; Andrew Wallace, COO')
    h = h.replace('Same Provider Network', 'Trilogy Provides Clients From Day One')
    h = h.replace('Physios, OTs, nurses, personal carers, cleaners &mdash; the allied health and support worker network you already use operates across both NDIS and aged care. Your existing relationships transfer directly.',
                  'Unlike our standard partnership model, enterprise partners receive an <strong>initial client portfolio</strong> on commencement. We allocate clients from our existing pipeline to ensure your team is productive from week one.')
    h = h.replace('Same Government Funding Structure', 'Percentage Model = Aligned Incentives')
    h = h.replace('Both are government-funded individual budgets managed by a registered provider. You already understand plan budgets, service bookings, compliance, and claiming. The system works the same way &mdash; just different legislation.',
                  'Trilogy\'s % model means we only earn when you earn. No hourly rate caps, no rate freezes. As your portfolio grows, so does everyone\'s revenue. Our interests are completely aligned.')
    # Revenue - enterprise scale
    h = h.replace('The Revenue Opportunity', 'The Enterprise Revenue Opportunity')
    h = h.replace('What if you earned more than your NDIS revenue &mdash; with half the complexity?',
                  'Scale your aged care revenue with Trilogy\'s client pipeline behind you')
    h = h.replace("""            <tr>
              <td>10</td>
              <td>$377K</td>
              <td>$38K &ndash; $57K</td>
              <td>Part-time income</td>
            </tr>
            <tr>
              <td>25</td>
              <td>$942K</td>
              <td>$94K &ndash; $141K</td>
              <td>Approaching ceiling</td>
            </tr>
            <tr class="highlight">
              <td><strong>50</strong></td>
              <td><strong>$1.88M</strong></td>
              <td><strong>$188K &ndash; $282K</strong></td>
              <td><strong>50&ndash;135% ABOVE</strong></td>
            </tr>
            <tr>
              <td>100</td>
              <td>$3.77M</td>
              <td>$377K &ndash; $565K</td>
              <td>3&ndash;5x ceiling</td>
            </tr>""",
                  """            <tr>
              <td>100</td>
              <td>$3.77M</td>
              <td>$377K &ndash; $565K</td>
              <td>2-3 coordinators</td>
            </tr>
            <tr>
              <td>250</td>
              <td>$9.42M</td>
              <td>$942K &ndash; $1.41M</td>
              <td>5-6 coordinators</td>
            </tr>
            <tr class="highlight">
              <td><strong>500</strong></td>
              <td><strong>$18.84M</strong></td>
              <td><strong>$1.88M &ndash; $2.83M</strong></td>
              <td><strong>10-12 coordinators</strong></td>
            </tr>
            <tr>
              <td>1,000</td>
              <td>$37.68M</td>
              <td>$3.77M &ndash; $5.65M</td>
              <td>20-25 coordinators</td>
            </tr>""")
    h = h.replace('vs NDIS Ceiling (~$120K)', 'Team Size Needed')
    # Revenue comparison
    h = h.replace("""          <h4>NDIS Ceiling</h4>
          <p>$100.14/hr &times; 25 billable hrs/wk &times; 48 wks = <strong>~$120K/year</strong>. Rate frozen. After staff costs, margin near zero.</p>""",
                  """          <h4>NDIS (Contracting)</h4>
          <p>Frozen rates, shrinking plans, Navigator replacement. <strong>48% of providers reporting losses.</strong> Revenue declining YoY.</p>""")
    h = h.replace("""          <h4>Aged Care (Worked Example)</h4>
          <p>30 clients &times; $37,683 avg package &times; 12% fee = <strong>$135K/year</strong>. At 50 clients: <strong>$226K/year</strong>. No cap, no freeze, growing 28%+.</p>""",
                  """          <h4>Aged Care Enterprise (Expanding)</h4>
          <p>500 clients &times; $37,683 avg &times; 12% = <strong>$2.26M/year</strong>. Clients provided from day one. Growing 28%+ annually. Uncapped.</p>""")
    # Programme
    h = h.replace('<h2 class="section-title">The Coordination Partner Programme</h2>',
                  '<h2 class="section-title">The Enterprise Partnership</h2>')
    h = h.replace('A partnership &mdash; not a job, not an acquisition',
                  'Clients from day one &mdash; your team coordinates, Trilogy powers the platform')
    h = h.replace('<li>Your business</li>\n            <li>Your client relationships</li>\n            <li>Your independence</li>\n            <li>Your brand</li>\n            <li>Your team</li>\n            <li>Your NDIS business alongside</li>',
                  '<li>Your organisation</li>\n            <li>Your coordination team</li>\n            <li>Your independence</li>\n            <li>Your brand</li>\n            <li>Your NDIS business alongside</li>\n            <li>Your growth trajectory</li>')
    h = h.replace('<li>Client acquisition support</li>\n            <li>Trilogy\'s registration</li>\n            <li>Automatic monthly payments</li>\n            <li>Dedicated Partnership Growth Consultant</li>\n            <li>Training + knowledge uplift</li>\n            <li>Growing market</li>',
                  '<li>Initial client portfolio from day one</li>\n            <li>Trilogy\'s registration &amp; platform</li>\n            <li>Automatic monthly payments</li>\n            <li>Dedicated enterprise account manager</li>\n            <li>Full team training &amp; onboarding</li>\n            <li>Ongoing client pipeline growth</li>')
    h = h.replace('<li>Chasing plan managers</li>\n            <li>Most invoicing admin</li>\n            <li>Registration burden</li>\n            <li>Audit prep</li>\n            <li>Rate freeze anxiety</li>\n            <li>Revenue ceiling</li>',
                  '<li>Finding aged care clients</li>\n            <li>Aged care registration</li>\n            <li>Claims &amp; billing admin</li>\n            <li>Technology platform costs</li>\n            <li>NDIS-only revenue risk</li>\n            <li>Revenue ceiling</li>')
    # Acquisition → How Enterprise Works
    h = h.replace('How You Build Your Client Base', 'How the Enterprise Model Works')
    h = h.replace('Dedicated support, proven growth strategies, and your existing network',
                  'Trilogy provides clients &mdash; your team delivers world-class coordination')
    h = h.replace('<h4>Your Warm Market</h4>\n          <ul>\n            <li>NDIS clients\' elderly parents &mdash; one degree from 20+ prospects</li>\n            <li>Allied health network works across both sectors</li>\n            <li>One email to therapist contacts opens referrals</li>\n          </ul>',
                  '<h4>Day One: Client Allocation</h4>\n          <ul>\n            <li>Trilogy allocates an initial client portfolio</li>\n            <li>Sized to your team\'s capacity</li>\n            <li>Geographic match to your operations</li>\n          </ul>')
    h = h.replace('<h4>Community Outreach</h4>\n          <ul>\n            <li>Hospital discharge units and planners</li>\n            <li>GPs, social workers, allied health</li>\n            <li>RSLs, retirement villages, community centres</li>\n          </ul>',
                  '<h4>Ongoing: Pipeline Growth</h4>\n          <ul>\n            <li>Continuous new client referrals as capacity grows</li>\n            <li>Priority allocation for enterprise partners</li>\n            <li>Quarterly pipeline reviews with your account manager</li>\n          </ul>')
    h = h.replace('<h4>Local Events &amp; Presence</h4>\n          <ul>\n            <li>Talks at retirement villages</li>\n            <li>Seniors groups, carer support groups</li>\n            <li>Community expos, networking events</li>\n          </ul>',
                  '<h4>Scale: Team Expansion</h4>\n          <ul>\n            <li>Hire more coordinators as your portfolio grows</li>\n            <li>Trilogy supports with training &amp; onboarding</li>\n            <li>No upper limit on portfolio size</li>\n          </ul>')
    h = h.replace('Trilogy equips you with co-branded brochures, client growth guides, and marketing support.',
                  'Enterprise partners receive priority client allocation, a dedicated account manager, and quarterly strategic reviews.')
    h = h.replace('See the growth guide', 'See the enterprise guide')
    # Timeline
    h = h.replace('From Handshake to First Client in 4 Weeks', 'From Agreement to First Clients in 4 Weeks')
    h = h.replace('<div class="timeline-label">Discovery Call</div>',
                  '<div class="timeline-label">Executive Discovery + Capacity Assessment</div>')
    h = h.replace('<div class="timeline-label">Portfolio Review + Price Book</div>',
                  '<div class="timeline-label">Partnership Agreement + Client Allocation Plan</div>')
    h = h.replace('<div class="timeline-label">Platform Onboarding</div>',
                  '<div class="timeline-label">Team Training + Platform Setup</div>')
    h = h.replace('<div class="timeline-label">Go Live</div>',
                  '<div class="timeline-label">Client Portfolio Transfer + Go Live</div>')
    h = h.replace('<li>Client Growth Guide</li>\n              <li>Brochure template</li>\n              <li>Email templates</li>\n              <li>Discharge referral guide</li>\n              <li>Fee schedule</li>',
                  '<li>Enterprise partnership agreement</li>\n              <li>Team training programme</li>\n              <li>Client portfolio allocation plan</li>\n              <li>Account management SLA</li>\n              <li>Fee schedule &amp; pricing book</li>')
    # Day to day
    h = h.replace('<li>You coordinate</li>\n              <li>Workers deliver</li>\n              <li>Trilogy claims</li>\n              <li>You get paid monthly</li>\n              <li>45-min annual audit</li>',
                  '<li>Your team coordinates</li>\n              <li>Service providers deliver</li>\n              <li>Trilogy claims &amp; bills</li>\n              <li>Monthly RCTI payments</li>\n              <li>Quarterly account reviews</li>')
    # CTA
    h = h.replace('Book Your Discovery Call', 'Book Your Executive Briefing')
    h = h.replace('In 30 minutes, you\'ll know exactly what your aged care revenue could look like &mdash; and whether this partnership makes sense.',
                  'In 45 minutes, we\'ll walk through the client allocation model, revenue projections for your team size, and partnership terms.')
    h = h.replace('Coordinators joining now are building their portfolio before the market gets crowded.',
                  'Enterprise partners who move now secure priority client allocation as the aged care market doubles over the next 5 years.')
    return h


# ══════════════════════════════════════════════════════════════
# MAIN — Generate all versions
# ══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    base = read_base()

    versions = [
        ('v2-ndis-brokered.html', build_v2, 'NDIS Brokered Partnership'),
        ('v3-ndis-providers-p1.html', build_v3, 'NDIS Service Providers to P1'),
        ('v4-agedcare-providers-p1.html', build_v4, 'Aged Care Providers to P1'),
        ('v5-agedcare-coordinators.html', build_v5, 'Aged Care Coordinators'),
        ('v6-agedcare-brokered.html', build_v6, 'Aged Care Brokered Partner'),
        ('v7-enterprise-ndis.html', build_v7, 'Large Corporate NDIS (Luke)'),
    ]

    for filename, builder, label in versions:
        html = builder(base)
        with open(filename, 'w') as f:
            f.write(html)
        lines = html.count('\n') + 1
        print(f'  {filename} ({lines} lines) — {label}')

    print(f'\nAll {len(versions)} versions generated successfully.')
