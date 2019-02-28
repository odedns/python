
import statistics


def calc_stats(bit_list):
    stats_dict = {}
    stats_dict['stddev'] = statistics.stdev(bit_list)
    stats_dict['mean']= statistics.mean(bit_list)
    stats_dict['variance']= statistics.variance(bit_list)

    curr_price = bit_list[-1]
    print(curr_price)
    profit = 0
    profit = [ (price-curr_price) for price in bit_list]
    stats_dict['profit'] = sum(profit)
    return stats_dict

