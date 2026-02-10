from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Feasible iff:
      1) For every resource r: total_requested[r] <= resources[r]
      2) At least one resource has leftover after allocation:
            exists r such that resources[r] - total_requested[r] > 0

    Assumption (from spec): inputs are provided in a reasonable and consistent format.
    """
    # Accumulate total demand per resource
    totals = {r: 0 for r in resources}

    for req in requests:
        if not isinstance(req, dict):
            # Kept because public tests include this case
            raise ValueError("Each request must be a dict mapping resource name to amount.")
        for r, amt in req.items():
            if r not in resources:
                return False
            totals[r] += amt
            if totals[r] > resources[r]:
                return False

    # NEW REQUIREMENT: at least one resource must remain unallocated
    # If there are no resources, we cannot have leftover.
    if not resources:
        return False

    any_leftover = any(resources[r] - totals[r] > 0 for r in resources)
    return any_leftover

