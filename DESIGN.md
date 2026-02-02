## Purpose & Scope
MetaGuard is a lightweight, rule-based transaction analysis tool designed to
identify clearly anomalous or suspicious transaction patterns in financial
metadata. It is intended as a first-line screening mechanism for financial fraud,
before much more complex tools are used.

MetaGuard is not - **and it's not trying to be** - a full solution for defense
against fraud, or a full replacement for human review. Instead, it can be used
for general screening (where use of more complex algorithms wouldn't be 
desirable, either for a lack of resources or time), or for education about 
heuristic algorithms and their use in fraud detection.

## Threat Model
We assume an adversary who:
- can perform transactions using compromised credentials
- may attempt rapid transactions across locations or devices

We do not assume:
- a more prepared and stealthy/long-term attack
- adversaries who deliberately tune their behavior to remain just below detection 
thresholds

These attack classes are considered out of scope for a lightweight,
rule-based screening system and would require more advanced detection
mechanisms.

The system assumes the adversary is economically motivated rather than
destructive, and thus attempts to maximize successful transactions while
minimizing detection.

## Detection Heuristics

### Geo-Velocity Check

Rationale:
Two distinct transactions at locations impossible to travel within a given
timeframe may indicate account compromise.

Assumption:
It's unlikely for a user to travel at speeds faster than that of a commercial
jet.

Limitations:
- the use of VPNs and other tools masking the real location of a user may trigger
false positives
- remote access attacks completely circumvent this check by sending transactions
directly from the victim’s device

### Frequency Spike

Rationale:
A large number of transactions may indicate a user account being compromised and
the attacker trying to quickly offload finances before the user notices.

Assumption:
A legitimate user is unlikely to suddenly start sending a large number of distinct
transactions withing a short timeframe.

Limitations:
- a user may very well need to send multiple transactions at once, like when they
receive their paycheck and immediately pay their fixed expenses (i. e. rent, loans)

### Device Stranger

Rationale:
A transaction being made from a different device immediately after another may
indicate user account has been compromised and accessed from the attackers
device.

Assumption:
A legitimate user is unlikely to switch devices between two subsequent purchases.

Limitations:
- the attacker may want to wait (for example until the user goes to sleep) to make
their move to increase the time they have before their actions are noticed
- this would again be circumvented by a remote access attack. This highlights that 
device- and location-based heuristics primarily detect credential misuse rather 
than full system compromise.

## Threshold selection

Thresholds are intentionally chosen conservatively to minimize false negatives.
Values such as the 800 km/h geo-velocity threshold are based on rough real-world
estimates (e.g. average commercial airliner speed).

For real-world deployment, these thresholds would require tuning based on
observed false positive and false negative rates. This data is not currently
available and would be gathered during operational use.

## Future improvements

- converting binary flags into a "fraud likelihood" score
- additional heuristic rules (e. g. uncharacteristically large transactions)
- support for multiple accounts
- a simple UI to make the software more accessible for the average user