import matchers as m

class QueryBuilder:
    def __init__(self, *matchers):
        if len(matchers)<1:
             self._matcher = m.All()
        elif len(matchers)<2:
            self._matcher = matchers
        else:
            self._matcher = m.And(matchers[0], matchers[1])

    def build(self):
        if not self._matcher:
            return m.All()
        return self._matcher

    def playsIn(self, team):
        return QueryBuilder(self._matcher, m.PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._matcher, m.HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._matcher, m.HasFewerThan(value, attr))


