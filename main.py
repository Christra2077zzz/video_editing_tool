def edit_video(video_name, audio_to_add_to_video, logo_to_add_to_video):
    video = path_to_raw_video + '/' + video_name
    clip = VideoFileClip(video)

    # Resize video
    if is_video_resize == 1:
        clip = clip.fx(vfx.resize, width=new_width, height=new_height)

    # Edit speed video
    clip = clip.fx(vfx.speedx, video_speed)
    print("Edit speed complete.")

    # Edit saturation video
    clip = clip.fx(vfx.colorx, video_color_effect)
    print("Edit color complete.")

    # Flip video
    if video_flip == 1:
        clip = clip.fx(vfx.mirror_x)
        print("Flip video complete.")

    # Add audio
    if add_sound == 1:
        audio_clip = AudioFileClip(path_to_audio + '/' + audio_to_add_to_video).set_duration(clip.duration)
        clip = clip.set_audio(audio_clip)
        clip = clip.volumex(video_volume)
        print("Edit audio complete.")

    # Add video logo (overlay video)
    if add_logo == 1:
        logo_video_path = path_to_logo + '/' + logo_to_add_to_video
        logo_clip = (VideoFileClip(logo_video_path)
                     .without_audio()
                     .resize(height=50)
                     .set_duration(clip.duration)
                     .set_pos(("right", "top")))
        print("Add video logo complete.")
        final_clip = CompositeVideoClip([clip, logo_clip])
    else:
        final_clip = clip

    final_clip.write_videofile(path_to_edited_video + '/' + video_name)
