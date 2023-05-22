import pytest

from src.controllers.receipecontroller import ReceipeController
from src.static.diets import Diet

# add your test case implementation here
@pytest.mark.unit

# Test case 1: 'diet' is not in 'receipe['diets']' list
def test_get_receipe_readiness_diet_not_in_diets_list():
    receipe = {
        'name': 'Chicken Stir Fry',
        'diets': ['gluten-free'],
        'ingredients': {
            'chicken': 2,
            'vegetables': 3,
            'soy sauce': 1,
            'garlic': 2
        }
    }
    available_items = {
        'chicken': 4,
        'vegetables': 5,
        'soy sauce': 1,
        'garlic': 3
    }
    diet = Diet('vegan')
    expected_result = None

    readiness = ReceipeController.get_receipe_readiness(receipe, available_items, diet)
    assert readiness == expected_result

# Test case 2: 'diet' is in 'receipe['diets']' list and 'calculate_readiness(receipe, available_items)' > 0.1
def test_get_receipe_readiness_diet_in_diets_list_and_readiness_greater_than_threshold():
    receipe = {
        'name': 'Chicken Stir Fry',
        'diets': ['gluten-free'],
        'ingredients': {
            'chicken': 2,
            'vegetables': 3,
            'soy sauce': 1,
            'garlic': 2
        }
    }
    available_items = {
        'chicken': 4,
        'vegetables': 5,
        'soy sauce': 1,
        'garlic': 3
    }
    diet = Diet('gluten-free')
    expected_result = 0.8

    readiness = ReceipeController.get_receipe_readiness(receipe, available_items, diet)
    assert readiness == expected_result

# Test case 3: 'diet' is in 'receipe['diets']' list and 'calculate_readiness(receipe, available_items)' <= 0.1
def test_get_receipe_readiness_diet_in_diets_list_and_readiness_less_than_threshold():
    receipe = {
        'name': 'Chicken Stir Fry',
        'diets': ['gluten-free'],
        'ingredients': {
            'chicken': 2,
            'vegetables': 3,
            'soy sauce': 1,
            'garlic': 2
        }
    }
    available_items = {
        'chicken': 1,
        'vegetables': 2,
        'soy sauce': 0,
        'garlic': 1
    }
    diet = Diet('gluten-free')
    expected_result = None

    readiness = ReceipeController.get_receipe_readiness(receipe, available_items, diet)
    assert readiness == expected_result
