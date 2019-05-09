<template>
  <div>
    <b-form-input class="form-input" v-model="filter" type="text" placeholder="Filter runs" />
    <b-list-group>
      <b-list-group-item v-for="run in filteredRuns" v-bind:key="run.name" @click="toggle(run)" v-bind:title="run.name">
        <input type="checkbox" v-model="run.visible" /> {{run.nameSimple}} <b-badge>{{run.date.fromNow()}}</b-badge> <b-badge>{{run.results.length}} epochs</b-badge>
        <b-button variant="default" v-b-modal.modal-1 @click="selectedRun = run">
          (more)
        </b-button>
      </b-list-group-item>
    </b-list-group>

    <b-modal title="Run inspector" size="xl" v-if="selectedRun" id="modal-1">
      <strong>Name:</strong> {{selectedRun.name}}<br>
      <strong>Ran for:</strong> {{selectedRun.results.length}} epochs<br>
      <strong>Configuration:</strong>
      <prism language="javascript">{{selectedRun.configuration}}</prism>
      <strong>Environment:</strong>
      <prism language="javascript">{{selectedRun.configuration}}</prism>
    </b-modal>
  </div>
</template>

<script>

import 'prismjs'
import 'prismjs/themes/prism.css'
import Prism from 'vue-prism-component'

export default {
  name: 'HelloWorld',
  props: {
    runs: Array
  },
  data() {
    return {
        filter: '',
        selectedRun: null
    }
  },
  computed: {
      filteredRuns: function() {
          return this.runs.filter((r) => { return new RegExp(this.filter).test(r.name) })
      }
  },
  methods: {
    toggle(run) {
      
      this.$set(run, 'visible', !run.visible);
      console.log("emite")
    }
  },
  components: {
    Prism
  }
}
</script>

<style scoped lang="scss">
</style>
