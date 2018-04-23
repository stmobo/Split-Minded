# When Calm wins the day 0 fight
label calm_day0_winner:
    "And that's how I kept control even after the others tried to kill me."

    calm "That was... frightening.{p}How did all of this happen?"

    pyro "Good show there, Mr. Calm."

    calm "Wait, what? I thought I..."

    pyro "As I said before, I don't think we can truly die.{p}We just fade, for a moment."

    calm "...so you all will be back to try and take over again."

    surv "You betcha."

    calm "Fuck."

    pyro "Rather unfortunately, I think it will take some time for us to reconstitute ourselves.{p}So we'll be seeing you later, rather than sooner."

    "...{p}I feel their presences vanish."

    "And with that out of the way, I guide [mc.name] back to sleep..."

    $ complete_fadeout()

    jump day1_start

# When Calm wins the day 1 morning fight
label calm_day1_start:
    return
