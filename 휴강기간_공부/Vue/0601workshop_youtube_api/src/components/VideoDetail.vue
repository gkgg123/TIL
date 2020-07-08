<template>
  <div >
    <div v-if="videoDetail" >
      <div class="embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item"  :src="youtubeUrl" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
      </div>
      
      <div>
        <li v-text="videoDetail.snippet.title"></li>
        <li v-text="videoDetail.snippet.description"></li>
      </div>
    
    </div>
    <div v-else>
     
    </div>
  </div>
</template>

<script>
export default {
  name:'VideoDetail',
  data(){
    return {
      videoId : 'M7lc1UVf-VE'
    }
  },
  props :{
    videoDetail : {
      type:Object,
    }
  },
  computed : {
    youtubeUrl(){
      const url = 'https://www.youtube.com/embed/'
      //return `https://www.youtube.com/embed/${this.videoDetail.id.videoId}`
      return url + this.videoDetail.id.videoId
    }
  },
}



</script>

<style>

</style>