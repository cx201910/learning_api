"""
WSGI config for ml_service project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ml_service.settings')

application = get_wsgi_application()


# ML registry
import inspect
from ml.registry import MLRegistry
from ml.income_classifier.random_forest import RandomForestClassifier
from ml.income_classifier.extra_trees import ExtraTreesClassifier

try:
    registry = MLRegistry() # Create  ML registry
    # Random Forest classifier and Extra Trees classifier
    rf = RandomForestClassifier()
    et = ExtraTreesClassifier()
    # Add  to ML registry
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Alex",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="testing",
                            algorithm_version="0.0.1",
                            owner="Alex",
                            algorithm_description="Extra Trees with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(ExtraTreesClassifier))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))