"""
统计上交所股票型ETF中涨停股和跌停股的持仓金额
"""
import akshare as ak
import pandas as pd
from datetime import datetime
import time

def get_limit_up_down_stocks():
    """获取今日涨停和跌停股票列表"""
    limit_up_stocks = set()
    limit_down_stocks = set()
    
    try:
        # 获取涨停股票
        limit_up_df = ak.stock_zt_pool_em(date=datetime.now().strftime('%Y%m%d'))
        if not limit_up_df.empty:
            limit_up_stocks = set(limit_up_df['代码'].tolist())
    except Exception as e:
        print(f"获取涨停股票失败: {e}")
    
    try:
        # 获取跌停股票 - 尝试不同的函数名
        try:
            limit_down_df = ak.stock_zt_pool_dtgc_em(date=datetime.now().strftime('%Y%m%d'))
        except:
            # 如果上面的函数不存在，尝试从A股实时行情中筛选
            all_stocks = ak.stock_zh_a_spot_em()
            # 跌停判断：涨跌幅 <= -9.9
            limit_down_df = all_stocks[all_stocks['涨跌幅'] <= -9.9]
        
        if not limit_down_df.empty:
            limit_down_stocks = set(limit_down_df['代码'].tolist())
    except Exception as e:
        print(f"获取跌停股票失败: {e}")
    
    return limit_up_stocks, limit_down_stocks

def get_sh_etf_list():
    """获取上交所股票型ETF列表 - 直接使用完整列表"""
    # 上交所常见股票型ETF完整列表
    etf_list = {
        '代码': [
            # 宽基指数ETF
            '510050', '510300', '510500', '510180', '510310', '510330', 
            '510900', '510210', '510800', '510850', '510020', '510090',
            '512100', '512910', '560010', '588000', '588080', '588050',
            # 行业ETF - 金融
            '510880', '512880', '512800', '512170', '512010', '512900',
            # 行业ETF - 消费
            '512690', '512600', '516110', '512980', '515170', '515650',
            # 行业ETF - 科技
            '515050', '515880', '512480', '512760', '516160', '515030',
            '515980', '512720', '512660', '515000', '512290', '512200',
            # 行业ETF - 医药
            '512170', '512010', '515120', '516390', '512290', '515950',
            # 行业ETF - 新能源
            '515790', '516580', '516850', '515700', '516930', '516150',
            '515220', '516670', '515210',
            # 行业ETF - 其他
            '512200', '515960', '512670', '515380', '515180', '512400',
            '512070', '515900', '512400', '515860', '516110', '516060',
            # 跨境ETF
            '513050', '513100', '513500', '513300', '513030', '513330',
            '513520', '513060', '513550', '513180', '513010', '513090',
            # 主题ETF
            '512580', '515850', '512190', '512170', '515390', '516970',
            '515600', '515070', '512560', '515710', '516510', '515230',
        ],
        '名称': [
            # 宽基指数ETF
            '50ETF', '300ETF', '500ETF', '180ETF', '300ETF易方达', '300ETF华泰',
            'H股ETF', '国企ETF', '中证100', '沪深300ETF', '超大盘ETF', '央企ETF',
            '1000ETF', '中证1000', '2000ETF', '科创50', '科创板50', '科创芯片',
            # 行业ETF - 金融
            '红利ETF', '证券ETF', '银行ETF', '医疗ETF', '医药ETF', '基建ETF',
            # 行业ETF - 消费
            '酒ETF', '食品ETF', '半导体', '传媒ETF', '食品饮料', '消费ETF',
            # 行业ETF - 科技
            '5GETF', '芯片ETF', '半导体ETF', '国防ETF', 'AIETF', '电子ETF',
            '人工智能', '计算机ETF', '软件ETF', '通信ETF', '创新药', '芯片龙头',
            # 行业ETF - 医药
            '医疗ETF', '医药ETF', '医疗健康', '生物医药', '创新药ETF', '医疗器械',
            # 行业ETF - 新能源
            '光伏ETF', '新能源车', '锂电ETF', '碳中和', '新能源', '电池ETF',
            '煤炭ETF', '有色金属', '稀土ETF',
            # 行业ETF - 其他
            '房地产', '钢铁ETF', '军工ETF', '环保ETF', '信息ETF', '有色ETF',
            '券商ETF', '恒生科技', '建材ETF', '游戏ETF', '工业ETF', '机械ETF',
            # 跨境ETF
            '中概互联', '纳指ETF', '标普500', '德国DAX', '日经ETF', '法国CAC',
            '恒生互联', '东证ETF', '亚太低碳', '港股通50', '港股通', '港股科技',
            # 主题ETF
            '养老ETF', '国企改革', '科技龙头', '医疗设备', '云计算', '数字经济',
            '新能源汽车', '家电ETF', '影视ETF', '物联网ETF', '旅游ETF', '化工ETF',
        ]
    }
    
    # 去重
    seen = set()
    unique_codes = []
    unique_names = []
    for code, name in zip(etf_list['代码'], etf_list['名称']):
        if code not in seen:
            seen.add(code)
            unique_codes.append(code)
            unique_names.append(name)
    
    df = pd.DataFrame({'代码': unique_codes, '名称': unique_names})
    print(f"使用本地ETF列表，共 {len(df)} 个上交所股票型ETF")
    return df

def get_etf_holdings(etf_code):
    """获取ETF持仓明细"""
    try:
        # 获取ETF持仓数据 - 使用正确的函数名
        time.sleep(0.5)  # 避免请求过快
        holdings_df = ak.fund_portfolio_hold_em(symbol=etf_code, date="")
        if not holdings_df.empty:
            print(f"  成功获取持仓数据，共 {len(holdings_df)} 只股票")
        return holdings_df
    except Exception as e:
        print(f"  获取持仓失败: {e}")
        return pd.DataFrame()

def calculate_etf_limit_holdings(etf_code, etf_name, limit_up_stocks, limit_down_stocks):
    """计算单个ETF持有的涨停股和跌停股金额"""
    holdings_df = get_etf_holdings(etf_code)
    
    if holdings_df.empty:
        return None
    
    # 打印列名以便调试（首次运行时可取消注释）
    # print(f"  持仓数据列: {holdings_df.columns.tolist()}")
    
    limit_up_amount = 0
    limit_down_amount = 0
    limit_up_count = 0
    limit_down_count = 0
    limit_up_stocks_detail = []
    limit_down_stocks_detail = []
    
    for _, row in holdings_df.iterrows():
        # 尝试获取股票代码（可能的列名）
        stock_code = None
        for col in ['股票代码', '代码', '证券代码']:
            if col in holdings_df.columns:
                stock_code = str(row[col]).strip()
                # 确保代码是6位数字
                if len(stock_code) == 6 and stock_code.isdigit():
                    break
                stock_code = None
        
        if not stock_code:
            continue
        
        # 尝试获取持仓市值占比
        ratio = 0
        for col in ['占净值比例', '持仓占比', '占比', '市值占比', '占净值比']:
            if col in holdings_df.columns:
                try:
                    val = row[col]
                    if isinstance(val, str):
                        val = val.replace('%', '')
                    ratio = float(val)
                    break
                except:
                    continue
        
        # 尝试获取持仓金额
        amount = 0
        for col in ['持仓市值', '市值', '持仓金额', '持仓市值(元)']:
            if col in holdings_df.columns:
                try:
                    amount = float(row[col])
                    break
                except:
                    continue
        
        # 获取股票名称
        stock_name = ""
        for col in ['股票名称', '名称', '证券名称']:
            if col in holdings_df.columns:
                stock_name = str(row[col])
                break
        
        if stock_code in limit_up_stocks:
            if amount > 0:
                limit_up_amount += amount
            limit_up_count += 1
            limit_up_stocks_detail.append(f"{stock_name}({stock_code})")
        elif stock_code in limit_down_stocks:
            if amount > 0:
                limit_down_amount += amount
            limit_down_count += 1
            limit_down_stocks_detail.append(f"{stock_name}({stock_code})")
    
    return {
        'ETF代码': etf_code,
        'ETF名称': etf_name,
        '涨停股数量': limit_up_count,
        '涨停股金额': limit_up_amount,
        '跌停股数量': limit_down_count,
        '跌停股金额': limit_down_amount,
        '涨停股明细': ', '.join(limit_up_stocks_detail) if limit_up_stocks_detail else '',
        '跌停股明细': ', '.join(limit_down_stocks_detail) if limit_down_stocks_detail else ''
    }

def main():
    print("=" * 60)
    print("上交所股票型ETF涨跌停持仓分析")
    print("=" * 60)
    
    # 1. 获取涨停和跌停股票
    print("\n正在获取涨停和跌停股票列表...")
    limit_up_stocks, limit_down_stocks = get_limit_up_down_stocks()
    print(f"涨停股票数量: {len(limit_up_stocks)}")
    print(f"跌停股票数量: {len(limit_down_stocks)}")
    
    # 2. 获取上交所股票型ETF列表
    print("\n正在获取上交所股票型ETF列表...")
    sh_etf_df = get_sh_etf_list()
    print(f"上交所股票型ETF数量: {len(sh_etf_df)}")
    
    # 3. 分析每个ETF的持仓
    print("\n正在分析ETF持仓...")
    results = []
    
    total_etfs = len(sh_etf_df)
    for idx, row in sh_etf_df.iterrows():
        etf_code = row['代码']
        etf_name = row['名称']
        print(f"[{idx+1}/{total_etfs}] 处理 {etf_code} - {etf_name}")
        
        result = calculate_etf_limit_holdings(etf_code, etf_name, limit_up_stocks, limit_down_stocks)
        if result:
            results.append(result)
        
        # 避免请求过快
        time.sleep(1)
    
    # 4. 整理结果并排序
    if results:
        result_df = pd.DataFrame(results)
        
        # 格式化金额显示（转换为万元）
        result_df['涨停股金额(万元)'] = (result_df['涨停股金额'] / 10000).round(2)
        result_df['跌停股金额(万元)'] = (result_df['跌停股金额'] / 10000).round(2)
        
        # 只显示有涨停或跌停持仓的ETF
        result_with_limit = result_df[(result_df['涨停股数量'] > 0) | (result_df['跌停股数量'] > 0)]
        
        # 按涨停股数量降序排序
        result_df_by_up = result_df.sort_values(['涨停股数量', '涨停股金额'], ascending=[False, False])
        print("\n" + "=" * 100)
        print("按涨停股数量排序（降序）- 仅显示有涨停持仓的ETF:")
        print("=" * 100)
        if len(result_with_limit[result_with_limit['涨停股数量'] > 0]) > 0:
            display_up = result_df_by_up[result_df_by_up['涨停股数量'] > 0][['ETF代码', 'ETF名称', '涨停股数量', '涨停股金额(万元)', '涨停股明细']]
            print(display_up.to_string(index=False))
        else:
            print("无ETF持有涨停股")
        
        # 按跌停股数量降序排序
        result_df_by_down = result_df.sort_values(['跌停股数量', '跌停股金额'], ascending=[False, False])
        print("\n" + "=" * 100)
        print("按跌停股数量排序（降序）- 仅显示有跌停持仓的ETF:")
        print("=" * 100)
        if len(result_with_limit[result_with_limit['跌停股数量'] > 0]) > 0:
            display_down = result_df_by_down[result_df_by_down['跌停股数量'] > 0][['ETF代码', 'ETF名称', '跌停股数量', '跌停股金额(万元)', '跌停股明细']]
            print(display_down.to_string(index=False))
        else:
            print("无ETF持有跌停股")
        
        # 汇总统计
        print("\n" + "=" * 100)
        print("汇总统计:")
        print("=" * 100)
        print(f"分析ETF总数: {len(result_df)}")
        print(f"持有涨停股的ETF数量: {len(result_df[result_df['涨停股数量'] > 0])}")
        print(f"持有跌停股的ETF数量: {len(result_df[result_df['跌停股数量'] > 0])}")
        print(f"涨停股总金额: {result_df['涨停股金额'].sum()/10000:.2f} 万元")
        print(f"跌停股总金额: {result_df['跌停股金额'].sum()/10000:.2f} 万元")
        
        # 保存结果到Excel
        output_file = f"ETF涨跌停持仓分析_{datetime.now().strftime('%Y%m%d')}.xlsx"
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # 完整数据 - 按涨停排序
            result_df_by_up.to_excel(writer, sheet_name='按涨停股排序(完整)', index=False)
            # 完整数据 - 按跌停排序  
            result_df_by_down.to_excel(writer, sheet_name='按跌停股排序(完整)', index=False)
            # 仅有涨跌停的ETF
            if len(result_with_limit) > 0:
                result_with_limit.sort_values(['涨停股数量', '跌停股数量'], ascending=[False, False]).to_excel(
                    writer, sheet_name='有涨跌停持仓的ETF', index=False)
        
        print(f"\n结果已保存到: {output_file}")
    else:
        print("\n未获取到有效数据")

if __name__ == "__main__":
    main()
