from collections import defaultdict, Counter
from itertools import combinations

class Solution:
    def mostVisitedPattern(
        self,
        username: list[str],
        timestamp: list[int],
        website: list[str]
    ) -> list[str]:
        visits = sorted(zip(timestamp, username, website))

        user_sites = defaultdict(list)

        for time, user, site in visits:
            user_sites[user].append(site)

        count = Counter()

        for sites in user_sites.values():
            patterns = set(combinations(sites, 3))

            for pattern in patterns:
                count[pattern] += 1

        max_score = max(count.values())

        return list(min(
            pattern for pattern, score in count.items()
            if score == max_score
        ))