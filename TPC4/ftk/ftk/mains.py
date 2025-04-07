import jjcli
import json
from ftk.base import Pipeline, Convert2ProbabilityStage
from ftk.probability import RelativeProbabilityPerMillion
from ftk.corpus import get_dictionary


def pretty_print(freqs, opts):
    freqs = dict(sorted(freqs.items(), key=lambda item: item[1].value, reverse=True))
    total = freqs[list(freqs.keys())[0]].total

    if "-a" not in opts:
        freqs = {key: RelativeProbabilityPerMillion(val) for key, val in freqs.items()}

    if "-m" in opts:
        m = int(opts["-m"])
        freqs = dict(list(freqs.items())[:m])

    freqs = {key: val.value for key, val in freqs.items()}
    if "-j" in opts:
        print(json.dumps({"total": total, "words": freqs}, indent=4))
    else:
        print(total)
        for key, val in freqs.items():
            print(f"{val}\t{key}")


def main():
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


def main_razoes():
    """Options:
    -l LANG: Specify the language identifier to use for the dictionary (default: 'pt' for Portuguese).
    """
    cl = jjcli.clfilter("l:", doc=main_razoes.__doc__)

    dic_geral = get_dictionary(cl.opt.get("-l", "pt"))
    pipe = Pipeline()
    pipe.set_reduction(Convert2ProbabilityStage())
    for txt in cl.text():
        txt_abs_freq = pipe.apply(txt)

        racios = []

        for word, freq in txt_abs_freq.items():
            freq_value = freq.value
            dic_value = dic_geral.get(word, 2).value

            print("freq", freq_value)
            print("dic", dic_value)

            if dic_value != 0:
                ratio = freq_value / dic_value
            else:
                ratio = 0

            print("freq/dic", ratio)
            racios.append((ratio, word))

        print(racios)


if __name__ == "__main__":
    main()
