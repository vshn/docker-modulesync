FROM ruby:2.5.1

LABEL maintainer "VSHN AG <tech@vshn.ch>"

COPY Gemfile Gemfile
RUN bundle install

CMD ["msync"]
