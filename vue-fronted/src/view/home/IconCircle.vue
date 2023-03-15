<template>
    <div>
        <transiton name="icon-circle-transition">
            <div ref="circle" class="icon_circle" @mouseover="iconMouseOver()" @mouseout="iconMouseOut()">
                <img src="../assets/注册.png">
            </div>
            <div class="tooltip" v-show="isOnIcon">{{ text }}</div>
        </transiton>
    </div>
</template>

<script>
export default {
    name: 'IconCircle',
    data() {
        return {
            isOnIcon: false,
        }
    },
    props: {
        imgSrc: String,
        text: String,
    },
    methods: {
        iconMouseOver() {
            this.isOnIcon = true;
            // 动画
            this.$refs.circle.style.transform = 'scale(1.2) translateX(-10px)';
            this.$refs.circle.style.transition = 'transform 0.3s';
        },
        iconMouseOut() {
            this.isOnIcon = false;
            // 动画
            this.$refs.circle.style.transform = 'scale(1) translateX(0)';
            this.$refs.circle.style.transition = 'none';
        }
    }
}

</script>

<style scoped>
.icon_circle {
    position: relative;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    z-index: 2;
}

.icon_circle img {
    width: 60%;
    height: 60%;
    object-fit: contain;
}

.tooltip {
    display: inline;
    position: absolute;
    top: 20%;
    left: 16%;
    width: 60px;
    border-radius: 50px;
    padding: 5px;
    background-color: #794B9C;
    color: #fff;
    z-index: -2;
}
</style>