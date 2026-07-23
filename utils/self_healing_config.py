"""
Self-Healing Configuration

Demo Mode intentionally makes the primary locator fail
so the healing engine can be demonstrated.

Turn OFF in production.
"""

SELF_HEALING_ENABLED = True

SELF_HEALING_DEMO = False

MAX_HEALING_ATTEMPTS = 5