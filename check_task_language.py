from libero.libero import benchmark
suite = benchmark.get_benchmark_dict()["libero_10"]()
for i, task in enumerate(suite.tasks):
    print(i, task.language)
