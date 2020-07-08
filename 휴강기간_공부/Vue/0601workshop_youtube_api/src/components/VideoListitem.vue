<template>

  <li class="list-group-item" @click="onVideoSelect">
    <div class="media" style="height:20vh">
      <img :src="thumbnailUrl" alt="" class="align-self-center mr-3">
      <div class="media-body">
       <div class="pt-auto border-bottom" style="height:5vh; font-size:1.5vh; "> <p style="text-overflow: ellipsis;">{{video.snippet.title}}</p></div>

       <div class="text-wrap w-100 text-break pt-4" style="font-size:1.5vh;
          height: 12vh;"><span>{{video.snippet.description}}</span></div>
      </div>
    </div>
  </li>
  
</template>

<script>
export default {
  name : 'VideoListitem',
  props : {
    video : {
      type : Object
    }
  },
  methods : {
    onVideoSelect(){
      this.$emit('video-select',this.video)
    },
  },
  computed :{
    thumbnailUrl(){
      return this.video.snippet.thumbnails.default.url
    }
  }

}
</script>

<style>

</style>