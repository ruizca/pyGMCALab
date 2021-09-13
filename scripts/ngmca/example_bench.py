# -*- coding: utf-8 -*-
from pyGMCA.bss.ngmca.core.benchmark import Benchmark
from pathlib import Path

# Load the provided configuration file
config_file = Path("benchmarks", "bench_db_basic.py")
config_file_abspath = config_file.absolute().as_posix()
bench = Benchmark(config_file_abspath)

# Compute the benchmark and save it in the "benchmarks" (relative) folder
bench.run("benchmarks")


# If the benchmark is already computed and saved,
# it is possible to reload it by providing the relative 
# path to the file.
benchmark_file = Path("benchmarks", "bench_S_tau_mad_P5MC12_04dec14_1042_820818.bch")
benchmark_file_abspath = benchmark_file.absolute().as_posix()
bench = Benchmark(benchmark_file_abspath)

# One can then display it with any display settings
bench.display(plottype="mean-std")
