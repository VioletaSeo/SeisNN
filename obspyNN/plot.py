import matplotlib.pyplot as plt
def plot_trace(trace):
    start_time = trace.stats.starttime
    pick_time = trace.pick.time - start_time
    pick_phase = trace.pick.phase_hint
    subplot = 2
    fig = plt.figure(figsize=(8, subplot * 2))

    ax = fig.add_subplot(subplot, 1, 1)
    ax.plot(trace.times(reftime=start_time), trace.data, "k-", label=trace.id)
    y_min, y_max = ax.get_ylim()
    ax.vlines(pick_time, y_min, y_max, color='r', lw=2, label=pick_phase)
    ax.legend()

    ax = fig.add_subplot(subplot, 1, subplot)
    ax.plot(trace.times(reftime=start_time), trace.pick.pdf, "b-", label=pick_phase + " pdf")
    ax.legend()
    plt.show()


def plot_stream(stream):
    for trace in stream:
        plot_trace(trace)
