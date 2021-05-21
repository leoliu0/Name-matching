abbr1 = [
    # corporation related words and some uninformative words
    ('the', ''),
    ('and', ''),
    ('of', ''),
    ('for', ''),
    ('llc', 'llc'),
    ('incorp\w+', 'inc'),
    ('CO', 'inc'),
    ('COS', 'inc'),
    ('companies', 'inc'),
    ('comapany', 'inc'),
    ('company', 'inc'),
    ('cor', 'inc'),
    ('CORP', 'inc'),
    ('corpor\w+', 'inc'),
    ('LTD', 'inc'),
    ('limit', 'inc'),
    ('limite', 'inc'),
    ('company incorp', 'inc'),
    ('incorp incorp', 'inc'),
    ('company limited', 'inc'),
    ('incorp limited', 'inc'),
    ('inc\s+inc', 'inc'),
    ('Assn', 'Association'),
    ('Assoc', 'Association'),
    ('intl', 'international'),
    ('interna\w+', 'international'),
    ('gbl', 'international'),
    ('global', 'international'),
    ('natl', 'national'),
    ('nat', 'national'),
    ('int', 'international'),
    ('&', 'and'),
    ('L\.P', 'LP'),
    ('L\.L\.P', 'LLP'),
    ('S\.A', 'SA'),
    ('S\.p\.A', 'SPA'),
    ('u s a', 'usa'),
    ('usa', 'usa'),
    ('u s', 'usa'),
    ('us', 'usa'),
    # Japanese suffix
    (r'(?!^|\w)kk', ''),
    (r'(?!^|\w)gk', ''),
    (r'(?!^|\w)yk', ''),
    (r'(?!^|\w)gmk', ''),
    (r'(?!^|\w)gsk', ''),
    (r'(?!^|\w)nk', ''),
    (r'(?!^|\w)tk', ''),
    (r'kanus\w+ kaisha', ''),
    # Germany suffix
    (r'(?!^|\w)ev', ''),
    (r'(?!^|\w)rv', ''),
    (r'(?!^|\w)kgaa', ''),
    ('gmbh co', ''),
    (r'(?!^|\w)ag co', ''),
    (r'(?!^|\w)se co', ''),
    ('gmbh', ''),
    (r'\bag', ''),
    (r'(?!^|\w)se', ''),
    (r'(?!^|\w)ug', ''),
    ('aktieng\w+', ''),
    # French suffix
    (r'(?!^|\w)sep', ''),
    (r'(?!^|\w)snc', ''),
    (r'(?!^|\w)scs', ''),
    (r'(?!^|\w)sca', ''),
    (r'(?!^|\w)sci', ''),
    (r'(?!^|\w)sarl', ''),
    (r'(?!^|\w)eurl', ''),
    (r'(?!^|\w)sa', ''),
    (r'(?!^|\w)s a', ''),
    (r'(?!^|\w)scop', ''),
    (r'\bsas$', ''),
    (r'\bsasu$', ''),
    # Swedish suffix
    (r'ab$', ''),
    (r'lm$', '')
]

abbr2 = [  # informative words
    ('univ', 'university'),
    ('bldg', 'building'),
    ('buildings', 'building'),
    ('MOR', 'Mortgage'),
    ('Banc', 'BankCorp'),
    ('bk', 'BankCorp'),
    ('bancshares ', 'bankcorp'),
    ('bankshares ', 'bankcorp'),
    ('BANC CORP', 'bankcorp'),
    ('BANCORPORATION', 'BankCorp'),
    ('bancorp', 'BankCorp'),
    ('stores', 'store'),
    ('brand', 'brands'),
    ('gen', 'general'),
    ('geneal', 'general'),
    ('Gereral', 'general'),
    ('Gereral', 'general'),
    ('generel', 'general'),
    ('solutions ', 'solution'),
    ('science', 'sciences'),
    ('sci', 'sciences'),
    ('work', 'works'),
    ('device', 'devices'),
    ('operation', 'operations'),
    ('tool', 'tools'),
    ('network', 'networks'),
    ('material', 'materials'),
    ('grp', 'group'),
    ('cap', 'capital'),
    ('FINL', 'financial'),
    ('THRU', 'Through'),
    ('COMM', 'Communication'),
    ('MGMT', 'Management'),
    ('INVT', 'investments'),
    ('INV', 'investments'),
    ('investment', 'investments'),
    ('PTNR', 'partner'),
    ('ADVR', 'advisors'),
    ('laboratory', 'laboratories'),
    ('lab', 'laboratories'),
    ('labs', 'laboratories'),
    ('ins', 'insurance'),
    ('insur', 'insurance'),
    ('insure', 'insurance'),
    ('technologies', 'tech'),
    ('technology', 'tech'),
    ('INDS', 'industries'),
    ('industry', 'industries'),
    ('indl', 'industries'),
    ('IND', 'industries'),
    ('res', 'research'),
    ('dev', 'development'),
    ('IP', ''),
    ('intellectual property', ''),
    ('intellectual properties', ''),
    ('intellectual', ''),
    (r'(?!^)patents', ''),
    (r'(?!^)patent', ''),
    (r'(?!^)trademark', ''),
    (r'(?!^)trademarks', ''),
    (r'(?!^)licensing', ''),
    #  ('marketing', ''),
    ('brands$', ''),
    ('property', 'properties'),
    ('Mort', 'Mortgage'),
    ('Thr', 'Through'),
    ('Sec', 'Securities'),
    ('RESOURCE', 'Resources'),
    ('Holding', 'Holdings'),
    ('Security', 'Securities'),
    ('ENTERPRISE', 'enterprises'),
    ('funding', 'fundings'),
    ('chem', 'chemical'),
    ('SYS', 'systems'),
    ('MFG', 'manufacturing'),
    ('Prod', 'products'),
    ('Pharma', 'Pharm'),
    ('Pharmaceu', 'Pharm'),
    ('Pharmaceuti', 'Pharm'),
    ('Pharmace', 'Pharm'),
    ('Pharmaceut', 'Pharm'),
    ('Pharmaceutical', 'Pharm'),
    ('Product', 'products'),
    ('svcs', 'services'),
    ('service', 'services'),
    ('production', 'productions'),
    ('saving', 'savings'),
    ('svgs', 'savings'),
    ('ln', 'loan'),
    ('electronic', 'electronics'),
    ('elect', 'electronics'),
    ('electrs', 'electronics'),
    ('elec', 'electric'),
    ('electrical', 'electric'),
    ('inst', 'institution'),
    ('motors', 'motor'),
    ('machine', 'machines'),
    ('machs', 'machines'),
    ('teleg', 'telegraph'),
    ('tel', 'telephone'),
    ('tel', 'telephone'),
    ('ry', 'railway'),
    ('american', 'america'),
    ('AMER', 'america'),
    ('AMERN', 'america'),
    ('phillip', 'philip'),
    (r'north\w* ameri\w+', 'america'),
]

# for some abbreviations, we have to hard code it.
hardcode = [
    ('hp hood', ''),
    ('hp pelzers?', ''),
    ('HP', 'HEWLETT PACKARD'),
    ('IBM', 'international business machines'),
    ('DE NEMOURS', ''),
    (r'\bE I\b', ''),
    ('NE NEMOURS', ''),
    (r'\bE I\b', ''),
    (r'\bEI\b', ''),
    (r'DU PONT', 'DU PONT'),
    (r'DU POND', 'DU PONT'),
    (r'DUPONT', 'DU PONT'),
    (r'DU PONTE', 'DU PONT'),
    ('HITACHI', 'HITACHI matchit'),
    ('exxon', 'exxon matchit'),
    ('SIEM\w+S', 'SIEMENS matchit'),
    ('GTE', 'GTE matchit'),
    ('north  america philips', 'philips'),
    ('toshiba', 'toshiba matchit'),
    ('Tokyo Shibaura', 'toshiba matchit'),
    ('merck', 'merck matchit'),
    ('eastm\w+ ko\w+', 'kodak'),
    ('kodak', 'kodak matchit'),
    ('canon', 'canon matchit'),
    ('Aluminum Company of America', 'alcoa'),
    ('alcoa', 'alcoa matchit'),
    ('hoescht', 'hoechst'),
    ('Hoeschst', 'hoechst'),
    ('Hoechet', 'hoechst'),
    ('Hoechset', 'hoechst'),
    ('hoechst', 'hoechst matchit'),
    ('International Telephone and Telegraph', 'IT'),
    #  ('rockwell','rockwell matchit'),
    ('nissan', 'nissan matchit'),
    ('ford meter box', ''),
    ('ford', 'ford matchit'),
    ('xerox', 'xerox matchit'),
    ('texaco', 'texaco matchit'),
    ('volvo', 'volvo matchit'),
    ('caterpillar', 'caterpillar matchit'),
]

suffix = set([
    'inc',
    'llc',
    'company',
    'limited',
    'trust',
    'lp',
    'llp',
    'sa',
    'spa',
    'usa',
    'holdings',
    'group',
    'enterprises',
    'gmbh',
    'kk',
    'and',
    'of',
    'north american',
    # Japanese suffix
    'kk',
    'gk',
    'yk',
    'gmk',
    'gsk',
    'nk',
    'tk',
    'Ka\w+ Kaisha',
    'aktieng\w+'
])
