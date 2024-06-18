import scipy.stats as stats
def calculate_probability(M, V, W):
      Z_W = (W - M) / (V**0.5)
      probability = 1 - stats.norm.cdf(Z_W)
      return round(probability, 2)
