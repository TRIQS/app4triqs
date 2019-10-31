#pragma once
#include "./types.hpp"
#include "./params.hpp"

namespace app4triqs {

  /// The Monte-Carlo Configuration Class
  struct qmc_config_t {

    //Constructor
    qmc_config_t(params_t const &params);
  };

} // namespace app4triqs
