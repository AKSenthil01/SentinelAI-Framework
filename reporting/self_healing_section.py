from utils.healing_logger import HealingLogger


class SelfHealingSection:

    @staticmethod
    def render():

        events = HealingLogger.get_events()

        if not events:

            return """
<section class="card">
<h2>Self-Healing Summary</h2>
<p>No locator recovery was required.</p>
</section>
"""

        rows = ""

        for event in events:

            rows += f"""
<tr>
<td>{event.original_locator}</td>
<td>{event.recovered_locator}</td>
<td>{event.source}</td>
</tr>
"""

        return f"""
<section class="card">

<h2>Self-Healing Summary</h2>

<table>

<tr>

<th>Original Locator</th>

<th>Recovered Locator</th>

<th>Recovery Source</th>

</tr>

{rows}

</table>

</section>
"""