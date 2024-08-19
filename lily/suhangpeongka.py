from collections import Counter

# Genetic Code 딕셔너리
genetic_code = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
}

def analyze_dna(dna_sequence):
    """
    분석할 DNA 서열을 입력받아 각 염기(A, T, C, G)의 개수를 반환합니다.
    
    :param dna_sequence: 분석할 DNA 서열 (문자열)
    :return: A, T, C, G의 개수를 담은 딕셔너리
    """
    nucleotide_count = Counter(dna_sequence)
    return nucleotide_count

def calculate_gc_content(dna_sequence):
    """
    DNA 서열에서 GC 함량을 계산합니다.
    
    :param dna_sequence: 분석할 DNA 서열 (문자열)
    :return: GC 함량 (부동 소수점 수)
    """
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    gc_content = (gc_count / len(dna_sequence)) * 100
    return gc_content

def calculate_sequence_length(dna_sequence):
    """
    DNA 서열의 길이를 계산합니다.
    
    :param dna_sequence: 분석할 DNA 서열 (문자열)
    :return: DNA 서열의 길이 (정수)
    """
    sequence_length = len(dna_sequence)
    return sequence_length

def translate_dna_to_protein(dna_sequence):
    """
    DNA 서열을 아미노산 서열(단백질 서열)로 번역합니다.
    
    :param dna_sequence: 분석할 DNA 서열 (문자열)
    :return: 아미노산 서열 (단백질 서열) 및 각 아미노산의 역할 (문자열)
    """
    protein_sequence = ''
    role_info = ''
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            protein_sequence += amino_acid
            role_info += f"{amino_acid}: {get_amino_acid_role(amino_acid)}\n"
        else:
            protein_sequence += '?'
            role_info += '?\n'
    return protein_sequence, role_info

def get_amino_acid_role(amino_acid):
    """
    아미노산이 하는 역할을 반환합니다.
    
    :param amino_acid: 아미노산 (문자열)
    :return: 아미노산의 역할 (문자열)
    """
    roles = {
        'A': '아라키돈산, 셀룰로오스 생합성의 단량체',
        'R': '암모니아와 탄소다이옥사이드를 사용하는 것은 생성이포아미딘산 합성',
        'N': '구조적인 역할을 하거나, 시스틴과 구합하는 등의 활동',
        'D': '글루타민산, 소포라 인산, 인산 제거에 사용',
        'C': '디아시갈기세리드 제조, 티아민 인산 제거에 사용',
        'E': '히스티딘의 영향을 받아 암모니아와 시스테인 생성',
        'Q': '카제인 및 피브로인의 구조적인 역할',
        'G': '글리시루신 생합성의 중간체',
        'H': '카르휘딘생합성에 사용',
        'I': '글리시네 제조, 및 시스테인생합성에 사용',
        'L': '리보세 제조, 및 프로틴 생합성에 사용',
        'K': '티로신 제조, 및 사이클로스포린생합성에 사용',
        'M': '암모니아를 사용하는 것은 생합성에 사용',
        'F': '프롤린 제조, 및 브롬산 생합성에 사용',
        'P': '피리드신 제조, 및 노르프레나린 생합성에 사용',
          'S': '세린의 생합성에 사용',
        'T': '시스테인의 생합성에 사용',
        'W': '트립토판의 생합성에 사용',
        'Y': '요오드화 타이로신 제조, 및 세린생합성에 사용',
        'V': '발린의 생합성에 사용',
        '*': '종결코돈',
        '?': '미지의 아미노산'
    }
    return roles.get(amino_acid, '미지의 아미노산')

# 사용자로부터 DNA 서열 입력 받기
dna_sequence = input("DNA 서열을 입력하세요: ")

# DNA 서열 분석하기
nucleotide_count = analyze_dna(dna_sequence)
gc_content = calculate_gc_content(dna_sequence)
sequence_length = calculate_sequence_length(dna_sequence)
protein_sequence, role_info = translate_dna_to_protein(dna_sequence)

# 결과 출력
print("A:", nucleotide_count['A'])
print("T:", nucleotide_count['T'])
print("C:", nucleotide_count['C'])
print("G:", nucleotide_count['G'])
print("GC 함량:", gc_content)
print("서열 길이:", sequence_length)
def translate_dna_to_protein(dna_sequence):
    """
    DNA 서열을 아미노산 서열(단백질 서열)로 번역합니다.
    
    :param dna_sequence: 분석할 DNA 서열 (문자열)
    :return: 아미노산 서열 (단백질 서열) 및 각 아미노산의 역할 (문자열)
    """
    protein_sequence = ''
    role_info = ''
    for i in range(0, len(dna_sequence) - 2, 3):  # 마지막 염기 서열이 3개 미만인 경우 제외
        codon = dna_sequence[i:i+3]
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            protein_sequence += amino_acid
            role_info += f"{amino_acid}: {get_amino_acid_role(amino_acid)}\n"
        else:
            protein_sequence += '?'
            role_info += '?\n'
    return protein_sequence, role_info
print("단백질 서열:", protein_sequence)
print("아미노산 역할:")
print(role_info)