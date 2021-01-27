# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis/
#
# Most of this work is copyright (C) 2013-2021 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.
#
# END HEADER

import hypothesis.strategies as st
from hypothesis.internal.conjecture.data import ConjectureData


def test_filter_iterations_are_marked_as_discarded():
    x = st.integers(0, 255).filter(lambda x: x == 0)

    data = ConjectureData.for_buffer([2, 1, 0])

    assert data.draw(x) == 0

    assert data.has_discards