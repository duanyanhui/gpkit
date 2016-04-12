"Implements TightConstraintSet"
from .set import ConstraintSet
from ..nomials import PosynomialInequality, SignomialInequality


class TightConstraintSet(ConstraintSet):
    "ConstraintSet whose inequalities must result in an equality."

    def __init__(self, constraints, substitutions=None, reltol=1e-6,
                 raiseerror=True):
        self.reltol = reltol
        self.raiseerror = raiseerror
        super(TightConstraintSet, self).__init__(constraints, substitutions)

    def process_result(self, result):
        "Checks that all constraints are satisfied with equality"
        super(TightConstraintSet, self).process_result(result)
        variables = result["variables"]
        for constraint in self.flat():
            if isinstance(constraint, (PosynomialInequality,
                                       SignomialInequality)):
                leftsubbed = constraint.left.sub(variables).value
                rightsubbed = constraint.right.sub(variables).value
                rel_diff = abs(1 - leftsubbed/rightsubbed)
                if rel_diff >= self.reltol:
                    if self.raiseerror is True:
                        raise ValueError("Tightness requirement not met"
                                         " for constraint %s because %s"
                                         " evaluated to %s but %s evaluated"
                                         " to %s"
                                         % (constraint,
                                            constraint.left, leftsubbed,
                                            constraint.right, rightsubbed))
                    else:
                        print "Warning: %s is not tight" % constraint
