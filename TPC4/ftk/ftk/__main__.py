import jjcli
import json
from base import Pipeline, Convert2ProbabilityStage
from probability import RelativeProbabilityPerMillion


def pretty_print(freqs: dict, opts: dict) -> None:
    if not freqs:
        print("No frequencies to display.")
        return

    from operator import itemgetter

    freqs = dict(
        sorted(freqs.items(), key=lambda item: itemgetter(1)(item).value, reverse=True)
    )
    total = next(iter(freqs.values())).total

    if "-a" not in opts:
        freqs = {key: RelativeProbabilityPerMillion(val) for key, val in freqs.items()}

    if "-m" in opts:
        try:
            m = int(opts.get("-m", 0))
            from itertools import islice

            freqs = dict(islice(freqs.items(), m))
        except ValueError:
            print("Invalid value for -m. Skipping top N filtering.")

    freqs = {key: val.value for key, val in freqs.items()}
    if "-j" in opts:
        print(json.dumps({"total": total, "words": freqs}, indent=4))
    else:
        print(total)
        for key, val in freqs.items():
            print(f"{val}\t{key}")


def main() -> None:
    """Options:
    -a: Display absolute frequencies instead of relative probabilities.
    -m N: Show only the top N most frequent words.
    -j: Output the results in JSON format.
    """

    cl = jjcli.clfilter("am:j", doc=main.__doc__)
    pipe = Pipeline()
    pipe.set_reduction(Convert2ProbabilityStage())

    for txt in cl.text():
        c = pipe.apply(txt)
        pretty_print(c, cl.opt)


if __name__ == "__main__":
    main()
