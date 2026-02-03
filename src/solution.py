## Student Name: Avery Backus
## Student ID: 219767888

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Rules implemented (based on the public tests + sensible constraints):
      - resources must be a dict[str, number] with non-negative capacities
      - requests must be a list of dict[str, number]
      - each request amount must be non-negative
      - if any request references a resource not present in resources -> infeasible (False)
      - allocation is feasible iff for every resource r:
            sum(request_i.get(r, 0)) <= resources[r]

    Returns:
        True if feasible, False otherwise.

    Raises:
        ValueError for malformed inputs (wrong types, non-numeric, negative values, etc.)
    """
    # Validate resources structure
    if not isinstance(resources, dict):
        raise ValueError("resources must be a dict mapping resource name to capacity")

    for k, v in resources.items():
        if not isinstance(k, str):
            raise ValueError("resource names in resources must be strings")
        if not isinstance(v, (int, float)):
            raise ValueError(f"capacity for resource '{k}' must be a number")
        if v < 0:
            raise ValueError(f"capacity for resource '{k}' must be non-negative")

    # Validate requests structure
    if not isinstance(requests, list):
        raise ValueError("requests must be a list of dicts")

    totals: Dict[str, float] = {r: 0.0 for r in resources}

    for idx, req in enumerate(requests):
        if not isinstance(req, dict):
            raise ValueError(f"request at index {idx} must be a dict")

        for rname, amount in req.items():
            if not isinstance(rname, str):
                raise ValueError(f"resource name in request at index {idx} must be a string")
            if not isinstance(amount, (int, float)):
                raise ValueError(f"amount for resource '{rname}' in request at index {idx} must be a number")
            if amount < 0:
                raise ValueError(f"amount for resource '{rname}' in request at index {idx} must be non-negative")

            if rname not in resources:
                # Requests a resource that doesn't exist in availability => infeasible
                return False

            totals[rname] += float(amount)

            # Early exit if we already exceed capacity
            if totals[rname] > float(resources[rname]):
                return False

    return True
