#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            row = list(map(int, line.strip().split(',')))
            data.append(row)
    return data

def calc_weighted_average(data_2d, weight):
    average = []
    for row in data_2d:
        weighted_sum = sum(x*w for x, w in zip(row, weight))
        average.append(weighted_sum)
    return average

def analyze_data(data_1d):
    n = len(data_1d)
    if n == 0:
        return 0, 0, 0, None, None
    
    sorted_data = sorted(data_1d)
    mean = sum(sorted_data) / n
    median = sorted_data[n // 2] if n % 2 != 0 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    var = sum((x - mean) ** 2 for x in sorted_data) / n
    
    return mean, var, median, min(sorted_data), max(sorted_data)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2:
        average = calc_weighted_average(data, [40/125, 60/100])
        with open('class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Total |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')
            
            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final'  : [f_score for _, f_score in data],
                'Average': average }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')

