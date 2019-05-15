<template>
  <div class="view-container" v-if="runs != null">
    <div class="side-left">
      <runs-list :runs="runs" />
    </div>
    <div class="middle">
      <b-btn @click="toggleLegend">Toggle legend</b-btn>
      <b-list-group>
        <b-list-group-item v-b-toggle.loss>
          Loss / val_loss
        </b-list-group-item>
        <b-collapse id="loss" visible>
          <b-list-group-item>
            <div class="chart-default">
              <GChart type="LineChart" :data="chartData" :options="chartOptions" />
            </div>
          </b-list-group-item>
        </b-collapse>

        <b-list-group-item v-b-toggle.accuracy>
          Accuracy
        </b-list-group-item>
        <b-collapse id="accuracy" visible>
          <b-list-group-item>
            <div class="chart-default">
              <GChart type="LineChart" :data="chartDataAccuracy" :options="chartOptionsAccuracy" />
            </div>
          </b-list-group-item>
        </b-collapse>

      </b-list-group>
    </div>
  </div>
</template>

<script>
import RunsList from './RunsList'
import moment from 'moment'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  components: {
    RunsList
  },
  data() {
    return {
      runs: [],
      chartData: [],
      chartDataAccuracy: [],
      chartOptions: {
        chart: {
          title: 'Loss / validation loss'
        },
        height: 650,
        explorer: {
          zoomDelta: 1.05
        },
        hAxis: {
          title: 'epochs'
        },
        vAxis: {
          title: 'loss'
        },
        chartArea: {
          left:100,
          top:100,
          right:300,
          bottom:100
        },
        legend: { position:'none' }
      },
      chartOptionsAccuracy: {
        height: 650,
        explorer: {
          zoomDelta: 1.05
        }
      }
    }
  },
  created () {
    this.fetch();
  },
  methods: {
    toggleLegend() {
      if(this.chartOptions.legend.position == 'none') {
        this.chartOptions.legend.position = 'outer';
        this.chartOptions.chartArea.right = 300;
      } else {
        this.chartOptions.legend.position = 'none';
        this.chartOptions.chartArea.right = 100;
      }
    },
    async fetch() {
      var runs = await fetch("http://192.168.1.67:5000/runs").then((r) => r.json());
      
      runs.forEach((r) => {
        r.date = moment(r.name, 'YYYYMMDD-HHmmss');
        r.nameSimple = r.name.replace(/^[0-9]+-[0-9]+-/gi, '');
      });

      runs = runs.sort((a,b) => a.date < b.date ? 1 : -1)

      this.runs = runs.filter((r) => r.results != null && r.results.length > 0); // we can't show runs without results
      console.log(runs)


    }
  },
  watch: {
    runs: {
      handler: function(newRuns) {
        var visibleRuns = newRuns.filter((r) => r.visible);
        var maxEpochCount = visibleRuns.map((r) => r.results.length).reduce(function(a, b) {
          return Math.max(a, b);
        }, 0);


        this.chartData = [
          [ "epoch", ...visibleRuns.map((r) => [`${r.name} loss`, `${r.name} val_loss`]).flat() ],
          ...[...Array(maxEpochCount).keys()].map((e) => [e, ...visibleRuns.map((r) => r.results.length <= e ? [null, null] : [parseFloat(r.results[e].loss), parseFloat(r.results[e].val_loss)]).flat()])
        ]

        var runsWithAccuracy = visibleRuns.filter(r => r.accuracies && r.accuracies.length)
        this.chartDataAccuracy = [
          [ "epoch", ...runsWithAccuracy.map((r) => [`${r.name} inst_sar`, `${r.name} inst_sdr`]).flat() ],
          ...[...Array(maxEpochCount).keys()].map((e) => [e, ...runsWithAccuracy.map((r) => (!r.accuracies || r.accuracies.length <= e) ? [null, null] : [parseFloat(r.accuracies[e].inst_sir), parseFloat(r.accuracies[e].inst_sdr)]).flat()])
        ]

      },
      deep: true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">


.view-container {
  margin:15px;
  display: grid;
  grid-template-columns: 400px auto;
  grid-column-gap: 20px;
}

.chart-default {
}
</style>
