from negmas import RankerNegotiator, MappingUtilityFunction, BinaryComparatorNegotiator
from negmas.st import VetoSTMechanism
from pytest import mark


@mark.parametrize("n_negotiators,n_outcomes", [(2,10), (3,50),(2,50), (3,5)])
def test_can_work(n_negotiators, n_outcomes):
    n_outcomes = 5
    mechanism = VetoSTMechanism(outcomes=n_outcomes, n_steps=3)
    ufuns = MappingUtilityFunction.generate_random(n_negotiators, outcomes=n_outcomes)
    for i in range(n_negotiators):
        mechanism.add(BinaryComparatorNegotiator(name=f"agent{i}"), ufun=ufuns[i])
    assert mechanism.state.step == 0
    mechanism.step()
    assert mechanism.state.step == 1
    assert mechanism.current_offer is not None
    mechanism.run()
    assert mechanism.agreement is not None

