# -*- coding: utf-8 -*-
"""
Created on Tue May 20 13:39:44 2025

@author: sdh
"""
from matplotlib.ticker import MultipleLocator, MaxNLocator, FuncFormatter
import math 

def set_tens_axis(ax, data, buffer=0.1):
    """
    항상 10의 배수로 y축을 조정하는 함수
    """
    data_min = min(data)
    data_max = max(data)
    data_range = data_max - data_min
    
    # 버퍼 추가
    y_min = data_min - data_range * buffer
    y_max = data_max + data_range * buffer
    
    # 10의 배수로 내림/올림
    y_min_rounded = math.floor(y_min / 10) * 10
    y_max_rounded = math.ceil(y_max / 10) * 10
    
    # y축 범위 설정
    ax.set_ylim(y_min_rounded, y_max_rounded)
    
    # 데이터 범위에 따라 주 눈금 간격 선택 (항상 10의 배수)
    if y_max_rounded - y_min_rounded > 100:
        major_interval = 50  # 큰 범위
    elif y_max_rounded - y_min_rounded > 50:
        major_interval = 20  # 중간 범위
    else:
        major_interval = 10  # 작은 범위
    
    # 주 눈금 설정 (항상 10의 배수)
    ax.yaxis.set_major_locator(MultipleLocator(major_interval))
    # 보조 눈금 설정
    ax.yaxis.set_minor_locator(MultipleLocator(major_interval/2))
    
    # 눈금 레이블 형식 설정 (항상 정수)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x)}"))
    
    return (y_min_rounded, y_max_rounded)