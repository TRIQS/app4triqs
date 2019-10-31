#pragma once
#include "./../qmc_config.hpp"

#include <triqs/mc_tools/random_generator.hpp>

namespace app4triqs::moves {

  /// A simple Monte-Carlo move
  struct insert {

    /// The Monte-Carlo configuration
    qmc_config_t &qmc_config;

    /// The random number generator
    triqs::mc_tools::random_generator &rng;

    /// Attempt vertex insertion
    mc_weight_t attempt();

    /// Accept vertex insertion
    mc_weight_t accept();

    /// Reject vertex insertion
    void reject();
  };

} // namespace app4triqs::moves
