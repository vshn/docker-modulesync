FROM ruby:2.5.1

LABEL maintainer "VSHN AG <tech@vshn.ch>"

WORKDIR /app
COPY Gemfile Gemfile
RUN bundle install

CMD ["msync"]
