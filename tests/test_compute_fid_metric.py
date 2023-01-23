# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest

import numpy as np
import torch

from generative.metrics import FID


class TestMMDMetric(unittest.TestCase):
    def test_results(self):
        x = torch.Tensor([[1, 2], [1, 2], [1, 2]])
        y = torch.Tensor([[2, 2], [1, 2], [1, 2]])
        results = FID()(x, y)
        np.testing.assert_allclose(results.cpu().numpy(), 0.4433, atol=1e-4)

    def test_input_dimensions(self):
        with self.assertRaises(ValueError):
            FID()(torch.ones([3, 3, 144, 144]), torch.ones([3, 3, 145, 145]))


if __name__ == "__main__":
    unittest.main()