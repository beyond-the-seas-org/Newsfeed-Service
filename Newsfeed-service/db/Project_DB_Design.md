## User Profile Service:

### Profile database

- `Student_Profile` (profile_id, name, email, ugrad_year_of_passing, masters_year_of_passing, ugrad_cgpa, masters_cgpa, GRE_score, github_link, linkdin_link, personal_website_link, current address, ugrad_university, masters_university, publication_id)

* [will there will be a "login_key" to find the authenticated person's profile?]
* [can there are more than one area of interset? if so, then we need another table]

- `Student_Publication` (profile_id, publication_link)

- `Student_Project` (profile_id, project_name, description, github_link)

- `Professor_shortlist` (profile_id, professor_id)

- `Area_of_interest`(id, name)

- `Student_Area_of_interest` (profile_id, area_of_interest_id)

- `Publication` (publication_id, link, date,desc)

- `Publication_Author` (publication_id(pk), author_id(pk), author_type(pk) (student/professor))


## News_feed service:

### News Feed Database

- `News_feed` (post_id, post, time, date, profile_id, community_id, type (newsfeed_post or community_post))[optional: react(up/down)]
- `News_feed_comments` (comment_id, comment, commenter_profile_id, post_id)[optional: react(up/down)]

## Explore Professors and Professor details

### Professor database

- `University_ranks` (uni_id(pk), name, area_of_interest_id(pk), rank)

- `Professor` (professor_id, name, email, address, university_id,)
- [can there are more than one area of interset?...if so ,then we need another table]

- `Professor_Area_of_interest` (professor_id, area_of_interest_id)

- `Professor_publication` (professor_id, publication_id, num_of_citation)

- `Professor_website_link` (professor_id, website_link, website_type) [as there could be different type of website_link (linkdin, personal, github etc)]

- `On_going_reserach` (on_going_research_id, research_field, research_topic, description, num_of_students, research_desc_link, funding_id)

- `On_going_Research_of_professors` (on_going_research_id, professor_id)

- `On_going_Research_of_students` (on_going_research_id, profile_id)

- `Funding` (Fundng_id, desc/funding_post, amount, requirement_description, num_of_slot, professor_id, availability(yes or no))
[can be NoSQL?]

- `Professor_Feedback` (feed_back_id, feedback, profile_id, professor_id)

## Preferance

- `Community` (community id,community name,Location_id)
- 
  `Location` (Location_id,Location_name,country,living_cost,weather,On campus job,Public transportation,home_community)

- `Hospital` (Hospital_id,hospital_name,Location_id)



