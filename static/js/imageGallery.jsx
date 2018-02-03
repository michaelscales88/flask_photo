import React, { Component } from 'react';
import ImageGallery from 'react-image-gallery';
import request from 'superagent';
import Image from './image.jsx'


export default class ImageGalleryComponent extends Component {

    constructor() {
        super();
        this.state = {
            showIndex: false,
            showBullets: true,
            infinite: true,
            showThumbnails: false,
            showFullscreenButton: true,
            showGalleryFullscreenButton: true,
            showPlayButton: true,
            showGalleryPlayButton: true,
            showNav: true,
            slideDuration: 450,
            slideInterval: 2000
        };
        this.images = this._getStaticImages();
    } s

    render() {
        return (
            <ImageGallery
                items={this.images}
                showIndex={this.state.showIndex}
                infinite={this.state.infinite}
                showThumbnails={this.state.showThumbnails}
                showFullscreenButton={this.state.showFullscreenButton}
                showGalleryFullscreenButton={this.state.showGalleryFullscreenButton}
                showPlayButton={this.state.showPlayButton}
                showGalleryPlayButton={this.state.showGalleryPlayButton}
                showNav={this.state.showNav}
                slideDuration={this.state.slideDuration}
                slideInterval={this.state.slideInterval}
                showBullets={this.state.showBullets}
                renderItem={this._renderImage.bind(this)} />
        );
    }

    _getStaticImages() {
        let images = [];
        request
            .get('/get-images')
            .then(function (res) {
                let data = res.body.data;
                for (let i = 0, len = data.length; i < len; i++) {
                    images.push({
                        original: "/image?" + $.param({ image: data[i].filename }),
                        originalAlt: data[i].filename,
                        description: data[i].description
                    });
                }
            })
            .catch(function (err) {
                // err.message, err.response
            });
        return images;
    }

    _renderImage(item) {
        return (
            <div className='image-gallery-image'>
                <Image src={item.original} width={item.width} height={item.height} mode='fill' /> 
            </div>
        );
    }
}